from django.contrib import admin

from .models import Patient, Trauma, Combine, History, GCS, Diagnosis, Injury, Monitor, Surgery, NonSurgicalTreatment, \
    Treatment, Assessment


class PatientAdmin(admin.ModelAdmin):
    pass


class TraumaAdmin(admin.ModelAdmin):
    pass


class CombineAdmin(admin.ModelAdmin):
    pass


class HistoryAdmin(admin.ModelAdmin):
    pass


class GCSAdmin(admin.ModelAdmin):
    pass


class DiagnosisAdmin(admin.ModelAdmin):
    pass


class InjuryAdmin(admin.ModelAdmin):
    pass


class MonitorAdmin(admin.ModelAdmin):
    pass


class SurgeryAdmin(admin.ModelAdmin):
    pass


class NonSurgicalTreatmentAdmin(admin.ModelAdmin):
    pass


class TreatmentAdmin(admin.ModelAdmin):
    pass


class AssessmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Patient, PatientAdmin)
admin.site.register(Trauma, TraumaAdmin)
admin.site.register(Combine, CombineAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(GCS, GCSAdmin)
admin.site.register(Diagnosis, DiagnosisAdmin)
admin.site.register(Injury, InjuryAdmin)
admin.site.register(Monitor, MonitorAdmin)
admin.site.register(Surgery, SurgeryAdmin)
admin.site.register(NonSurgicalTreatment, NonSurgicalTreatmentAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Assessment, AssessmentAdmin)
