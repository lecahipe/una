import factory
from data.models import UserDeviceMetabolicData

class UserDeviceMetabolicDataFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserDeviceMetabolicData

    user_id = factory.Faker('uuid4')
    device = factory.Faker('word')
    device_serialnumber = factory.Faker('ean13')
    device_timestamp = factory.Faker('date_time_this_decade')
    recording_type = factory.Faker('random_int', min=70, max=180)
    glucose_value_history = factory.Faker('random_int', min=70, max=180)
    glucose_scan = factory.Faker('random_int', min=70, max=180)
    non_numeric_rapid_acting_insulin = factory.Faker('word')
    fast_acting_insulin_units = factory.Faker('random_int', min=1, max=10)
    non_numeric_food_data = factory.Faker('word')
    carbohydrates_grams = factory.Faker('random_int', min=0, max=100)
    carbohydrates_servings = factory.Faker('random_int', min=0, max=10)
    non_numeric_depot_insulin = factory.Faker('word')
    depot_insulin_units = factory.Faker('random_int', min=1, max=10)
    notes = factory.Faker('sentence')
    glucose_test_strips = factory.Faker('random_int', min=70, max=180)
    ketone_mmol = factory.Faker('pydecimal', left_digits=2, right_digits=2, positive=True)
    meal_insulin_units = factory.Faker('random_int', min=1, max=10)
    correction_insulin_units = factory.Faker('random_int', min=1, max=10)
    insulin_change_by_user_units = factory.Faker('random_int', min=1, max=10)
    creation_timestamp = factory.Faker('date_time_this_decade')