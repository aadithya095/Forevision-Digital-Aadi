from django.core.exceptions import ValidationError
from models.tags import Tags
import datetime

'''
    NOTE: This file Contains Custom Validators for Forms
    TODO: create Validators for Image Limit Maximum size to 10MB and 3000 x 3000 px Resolution

'''


class MethodForm:

    # To Add Extra None Value to Select fild Choices for ID_TYPE
    def formIdTypehoice():
        idTuple = Tags.ID_TYPE_CHOICE
        idList = list(idTuple)
        idList.insert(0, ('None', '---------'))
        idTuple = tuple(idList)

        return idTuple

    # Raise Error if ID SelectField is None
    def checkIdType(value):
        if value == 'None':
            raise ValidationError('Please select proper id type.')

    def validateDateRange(value):
        if value > datetime.date.today() or value < datetime.date(1900, 1, 1):

            raise ValidationError(f'This Date is Invalid!: {value}')

    # Checks File Format and Limit Maximum size for songField
    def clean_file(value):
        if value:
            if not value.name.endswith(('.mp3', '.wav')):
                raise ValidationError(
                    "File format is not supported. Please upload an .mp3 or .wav file.")
            elif value.size > 100 * 1024 * 1024:  # 10 MB
                raise ValidationError(
                    "File size is too large. Please upload a file smaller than 10 MB.")

        return value
