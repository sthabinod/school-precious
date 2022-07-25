from django.contrib import admin

from account.models import Bus, BusCategory, Chat, EntranceRegister, ParentProfile, ScholarshipRegister, StudentProfile, TeacherLeave, TeacherProfile,Class

@admin.register(EntranceRegister)
class EntranceAdmin(admin.ModelAdmin):
    pass

@admin.register(ScholarshipRegister)
class ScholarshipAdmin(admin.ModelAdmin):
    pass


@admin.register(TeacherLeave)
class TeacherLeaveAdmin(admin.ModelAdmin):
    list_display=['teacher_user','is_approved']

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    # list_display=['teacher_user','is_approved']
    pass

@admin.register(BusCategory)
class BCAdmin(admin.ModelAdmin):
    # list_display=['teacher_user','is_approved']
    pass



@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    # list_display=['teacher_user','is_approved']
    pass


@admin.register(ParentProfile)
class ParentAdmin(admin.ModelAdmin):
    # list_display=['teacher_user','is_approved']
    pass

@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    # list_display=['teacher_user','is_approved']
    pass


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    pass


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    pass



