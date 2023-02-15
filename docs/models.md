# Developers Guide on How to Use Models

Models are the object representation of the database in pythonic form that can 
be used and integrated easily with the framework. Django basically provides an 
easy API to interact and deal with the database without even delving deeper 
into database queries.

The models for this project are seperated into two types. Models that are for 
user side to access and models that are for admin to access. The models for 
user are seperated in a module called `ddex_models.py` and models for admins to 
access are in `admin_models.py`.

All the models lives in the `models` app in `src` directory.

## Architecture of Database
The database consists of the 6 entities in total excluding the database design 
for Users models. They are:
    - Order
    - Party
    - Song
    - Album
    - Image
    - Clip

### Order
The Order model consists of the following attribute.
    - plan_choice
    - release_type

### Party
The Party model consists of the following attribute.
    - party_type
    - role
    - name
    and a method to give reference id of the party

### Song
The Song model consists of the following attribute.
    - id_type
    - id_value
    - name
    - audio_file
    - has_crbt (bool)
    - crbt_start_time (opt)
    - crbt_code (opt)
    - has_clip (bool)
    - album (fk)
    - order (fk)
    - party (m2m)

### Album
The Album model consists of the following attribute.
    - id_type
    - id_value
    - name
    - order (fk)

### Image
The Image model consists of the following attribute.
    - id_type
    - id_value
    - name
    - image_file
    - song (fk)

### Clip
The Clip model consists of the following attribute.
    - audio_file
    - name
    - song (fk)

## Accessing Data and making queries
The data can be accessed by in the following way:
```python
class Clip(models.Model):
    audio_file = models.FileField()
    name = models.CharField()
    song = models.ForeignKey(Song)
```

To access all the clips in the database we use:
```python
clips = Clip.objects.all()
```

To get specific data using id's we use:
```python
clip = Clip.objects.get(pk=1)
```
In this case we also have a foreign key on song which means clip and song has
one to one relationship.

A foreignkey can be used to address one to many relationships as well as one
to one relationships.

To access all clips from song we make use if sets that is provided by django.
```python
song = Song.objects.all()[0]
song_specific_clip = song.clip_set.all()

# with clip
clip = Clip.objects.all()[0]
songs = clip.song.all()
```

