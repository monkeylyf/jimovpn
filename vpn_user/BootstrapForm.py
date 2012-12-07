from django.forms import CharField, Form
from django.forms.forms import BoundField
from django.forms.util import ErrorList
from django.template import Context, Template
 

class BootstrapForm(Form):
    template = \
u'''
{%if top_errors%}
  <ul class="errorlist">
  {%for err in top_errors%}
    <li>{{err}}</li>
  {% endfor %}
  </ul>
{%endif%}

{%for field in form%}
<div class="control-group {%if field.errors%}error{%endif%}">
{{field.label_tag}}
<div class="controls">
{{field}}<span class="help-inline">{{field.errors}}</span>
</div>
</div>
{% endfor %}
'''
 
    def __unicode__(self):
        top_errors = self.non_field_errors() # Errors that should be displayed above all fields.
        c = Context({'form': self, 'top_errors': top_errors})
        t = Template(self.template)
        return t.render(c)
 
def decorate_label_tag(f):
 
    def bootstrap_label_tag(self, contents=None, attrs=None):
        attrs = attrs or {}
        add_class(attrs, 'control-label')
        return f(self, contents, attrs)
 
    return bootstrap_label_tag
 
 
BoundField.label_tag = decorate_label_tag(
         BoundField.label_tag)
 
 
def add_class(attrs, html_class):
    assert type(attrs) is dict
 
    if 'class' in attrs:
        classes = attrs['class'].split()
        if not html_class in classes:
            classes.append(html_class)
            attrs['class'] = ' '.join(classes)
    else:
        attrs['class'] = html_class
