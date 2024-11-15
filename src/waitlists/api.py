from ninja import Router
from typing import List
from .schemas import WaitListEntryListSchema,WaitListEntryDetailSchema
from .models import WaitListEntry
from django.shortcuts import get_object_or_404
router=Router()

@router.get("",response=List[WaitListEntryListSchema])
def list_waitList_entries(request):
    qs=WaitListEntry.objects.all()
    return qs

@router.get("/{entry_id}",response=WaitListEntryDetailSchema)
def get_waitList_entry(request,entry_id:int):
    obj=get_object_or_404(WaitListEntry,id=entry_id)
    return obj