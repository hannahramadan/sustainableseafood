from wtforms import Form, StringField, SelectField

class FishSearchForm(Form):
    choices = [('Fish', 'Fish'),
               ('Region', 'Region')]
    select = SelectField('Search for fish:', choices=choices)
    search = StringField('')