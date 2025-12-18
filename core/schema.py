from ninja import ModelSchema
from .models import State, Taxes, Accounts


class StateListSchema(ModelSchema):
    class Meta:
        model = State
        fields = "__all__"
        exclude = ["id"]
        
class TaxListSchema(ModelSchema):
    class Meta:
        model = Taxes
        fields = "__all__"
        exclude = ["id"]

class AccountListSchema(ModelSchema):
    class Meta:
        model = Accounts
        fields = "__all__"
        exclude = ["id"]

