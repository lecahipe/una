from django.db import models


class UserDeviceMetabolicData(models.Model):
    '''
        Model for the UserDeviceMetabolicData table
    '''
    user_id = models.UUIDField(db_index=True) # Should be a foreign key to the User model
    device = models.CharField(max_length=100)  # Should be a foreign key to the Device model
    device_serialnumber = models.CharField(max_length=100) # Not necessary if device is a foreign key
    device_timestamp = models.DateTimeField()
    recording_type = models.SmallIntegerField()
    glucose_value_history = models.DecimalField(max_digits=5, decimal_places=2, db_index=True, null=True, blank=True)
    glucose_scan = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    non_numeric_rapid_acting_insulin = models.CharField(max_length=255, null=True, blank=True)
    fast_acting_insulin_units = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    non_numeric_food_data = models.TextField(null=True, blank=True)
    carbohydrates_grams = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    carbohydrates_servings = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    non_numeric_depot_insulin = models.CharField(max_length=255, null=True, blank=True)
    depot_insulin_units = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    glucose_test_strips = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    ketone_mmol = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    meal_insulin_units = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    correction_insulin_units = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    insulin_change_by_user_units = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    creation_timestamp = models.DateTimeField(auto_now_add=True)

