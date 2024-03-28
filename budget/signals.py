from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from .models import Budget, Transaction, BudgetLabel, BudgetCategory
from django.dispatch import receiver


@receiver(pre_save, sender=Transaction)
def change_transaction(sender, instance, **kwargs):
    if Transaction.objects.filter(id=instance.id).exists():
        budget = instance.label.category.budget
        old_transaction = Transaction.objects.get(pk=instance.id)
        if instance.incoming == True:
            if instance.deleted_status == True and instance.deleted_status != old_transaction.deleted_status:
                budget.total_budget = budget.total_budget + instance.amount
            elif instance.deleted_status == False and instance.deleted_status != old_transaction.deleted_status:
                budget.total_budget = budget.total_budget - instance.amount
            else:
                budget.total_budget = budget.total_budget + old_transaction.amount
                instance.label.received = instance.label.received - old_transaction.amount
                instance.label.category.received = instance.label.category.received - old_transaction.amount
                instance.label.save()
            budget.save()
        else:
            if instance.deleted_status == True and instance.deleted_status != old_transaction.deleted_status:
                budget.total_budget = budget.total_budget + old_transaction.amount
            elif instance.deleted_status == False and instance.deleted_status != old_transaction.deleted_status:
                budget.total_budget = budget.total_budget - old_transaction.amount
            else:
                instance.label.received = instance.label.received - old_transaction.amount
                instance.label.category.received = instance.label.category.received - old_transaction.amount
                instance.label.save()
            budget.save()


@receiver(post_save, sender=Transaction)
def add_transaction(sender, instance, created, **kwargs):
    if created:
        budget = instance.label.category.budget
        if instance.incoming == True:
            budget.total_budget = instance.amount + budget.total_budget
            budget.save()
        else:
            budget.total_budget = budget.total_budget - instance.amount
            budget.save()

        instance.label.received = instance.label.received + instance.amount
        instance.label.category.received = instance.label.category.received + instance.amount
        instance.label.save()


@receiver(pre_save, sender=BudgetLabel)
def add_label(sender, instance, **kwargs):
    category = instance.category
    category.planned = category.planned + instance.planned
    category.save()

@receiver(pre_save, sender=BudgetLabel)
def change_label(sender, instance, **kwargs):
    if BudgetLabel.objects.filter(id=instance.id).exists():
        old_planned = BudgetLabel.objects.get(pk=instance.id)
        category = instance.category
        category.planned = category.planned - old_planned.planned
        category.save()

@receiver(pre_delete, sender=BudgetLabel)
def delete_label(sender, instance, **kwargs):
    category = instance.category
    category.planned = category.planned - instance.planned
    category.save()

@receiver(pre_delete, sender=Transaction)
def delete_transaction(sender, instance, **kwargs):
    budget = instance.label.category.budget
    old_budget = Budget.objects.get(id=instance.label.category.budget.id)
    if instance.incoming == True:
        instance.label.category.budget.total_budget = old_budget.total_budget - instance.amount
        instance.save()
    else:
        instance.label.category.budget.total_budget = old_budget.total_budget + instance.amount
        instance.save()

    instance.label.received = instance.label.received - instance.amount
    instance.label.category.received = instance.label.category.received - instance.amount
    instance.save()