# Templatetags

Template tags are tags that can be used in templates to do something with the arguments provided. It can render, add styles and perform logic with the given object. All template tags and its associated documentation can be found on the `/templatetags/` directory.

1. addcss
`addcss` template tag is used to apply css class to a formfield. A form field can be any input fields eg: password, username, etc.

Usage:
```
{{ form_field.username|addcss:'form-table'  }}
```
