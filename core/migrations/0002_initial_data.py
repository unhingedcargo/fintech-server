import csv
from pathlib import Path
from django.db import migrations

def load_data(apps, schema_editor):
    State = apps.get_model('core', 'State')
    Taxes = apps.get_model('core', 'Taxes')
    Accounts = apps.get_model('core', 'Accounts')

    BASE_DIR = Path(__file__).resolve().parent.parent

    state_csv = BASE_DIR / 'fixtures' / 'states.csv'
    states_list = []

    try:
        with open(state_csv, 'r') as statefile:
            reader = csv.DictReader(statefile)

            for row in reader:
                states_list.append(
                    State(
                        name = row['name'],
                        gst_code = row['gst_code']
                    )
                )
        
        if states_list:
            State.objects.bulk_create(states_list)
    except FileNotFoundError:
        print("states.csv file not found in core/fixtures/states.csv")

        
    tax_csv = BASE_DIR / 'fixtures' / 'taxes.csv'
    taxes_list = []

    try:
        with open(tax_csv, 'r') as taxfile:
            reader = csv.DictReader(taxfile)

            for row in reader:
                taxes_list.append(
                    Taxes(
                        tax = row['tax'],
                        rate = row['rate']
                    )
                )
        
        if taxes_list:
            Taxes.objects.bulk_create(taxes_list)
    except FileNotFoundError:
        print("taxes.csv file not found in core/fixtures/taxes.csv")

        
    accounts_csv = BASE_DIR / 'fixtures' / 'accounts.csv'
    accounts_list = []

    try:
        with open(accounts_csv, 'r') as accountsfile:
            reader = csv.DictReader(accountsfile)

            for row in reader:
                accounts_list.append(
                    Accounts(
                        name = row['name'],
                        txn_type = row['txn_type']
                    )
                )
        
        if accounts_list:
            Accounts.objects.bulk_create(accounts_list)
    except FileNotFoundError:
        print("accounts.csv file not found in core/fixtures/accounts.csv")
    except Exception as e:
        print(f"Exception error : {e}")

        
class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]