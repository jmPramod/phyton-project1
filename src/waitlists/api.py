from ninja import Router
from typing import List
from .schemas import WaitListEntryListSchema
from .models import WaitListEntry

router=Router()

@router.get("",response=List[WaitListEntryListSchema])
def list_waitList_entries(request):
    qs=WaitListEntry.objects.all()
    return qs