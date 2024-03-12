from django.db.models.signals import post_save, pre_save
from .models import Budget, Transaction, BudgetLabel, BudgetCategory
from django.dispatch import receiver


@receiver(pre_save, sender=Transaction)
def change_transaction(sender, instance, **kwargs):
    if Transaction.objects.filter(id=instance.id).exists():
        budget = instance.label.category.budget
        old_transaction = Transaction.objects.get(pk=instance.id)
        if instance.incoming == True:
            budget.total_budget = budget.total_budget - old_transaction.amount
            budget.save()
        else:
            budget.total_budget = budget.total_budget + old_transaction.amount
            budget.save()
        instance.label.received = instance.label.received - old_transaction.amount
        instance.label.category.received = instance.label.category.received - old_transaction.amount
        instance.label.save()


@receiver(post_save, sender=Transaction)
def change_budget(sender, instance, **kwargs):
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


@receiver(post_save, sender=BudgetLabel)
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