from django.contrib import admin
from Blog.models import Answer, Question
from Accounts.models import Lawyer_identification


admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Lawyer_identification)

