import json
import datetime
import decimal

from django.http import HttpResponse
from django.db.models.fields.related import ManyToManyField

class DjangoJSONEncoder(json.JSONEncoder):
    """
    JSONEncoder subclass that knows how to encode date/time and decimal types.
    """
    def default(self, o):
        # See "Date Time String Format" in the ECMA-262 specification.
        if isinstance(o, datetime.datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(o, datetime.date):
            return o.strftime("%Y-%m-%d")
        elif isinstance(o, datetime.time):
            if is_aware(o):
                raise ValueError("JSON can't represent timezone-aware times.")
            return o.strftime("%H:%M:%S")
        elif isinstance(o, decimal.Decimal):
            return str(o)
        else:
            return super(DjangoJSONEncoder, self).default(o)

def tojson(obj):
    return json.dumps(obj, cls=DjangoJSONEncoder)

def render_to_json(obj, status, msg):
    obj["status"] = status
    obj["msg"] = msg
    return HttpResponse(tojson(obj))

def get_value_from_model(model, field):
    parts = field.split(".", 1)
    value = getattr(model, parts[0])
    if len(parts) == 2:
        value = get_value_from_model(value, parts[1])
    return value

def model_to_dict(instance, fields=None):
    opts = instance._meta
    data = {}
    if fields is None:
        fields = [f.attname for f in opts.fields]
    for f in fields:
        data[f] = get_value_from_model(instance, f)
    return data


