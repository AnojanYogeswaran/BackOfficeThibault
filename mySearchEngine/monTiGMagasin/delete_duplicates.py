from django.db.models import Count

from models import InfoProduct

duplicate_tig_ids = InfoProduct.objects.values('tig_id').annotate(tig_id_count=Count('tig_id')).filter(tig_id_count__gt=1).values_list('tig_id', flat=True)
for tig_id in duplicate_tig_ids:
    products_to_delete = InfoProduct.objects.filter(tig_id=tig_id).order_by('id')[1:]
    products_to_delete.delete()

