from django.contrib import admin
from .models import Project, Skill, Experience, Contact


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'order', 'created_at']
    list_editable = ['is_featured', 'order']
    search_fields = ['title', 'description']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_editable = ['proficiency', 'order']
    list_filter = ['category']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['role', 'company', 'duration', 'order']
    list_editable = ['order']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'submitted_at', 'is_read']
    list_filter = ['is_read']
    readonly_fields = ['name', 'email', 'message', 'submitted_at']
