from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'bank'
        ordering = ['name']  # ascending ordering

    def __str__(self):
        return "{}".format(self.name)

    def __unicode__(self):
        return self.name


class Branch(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=15)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch = models.CharField(max_length=150)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=30)

    class Meta:
        db_table = 'branch'
        ordering = ['state', 'city', 'district', 'branch']

    def __unicode__(self):
        return 'IFSC: {}, Bank:{}, Branch'.format(self.ifsc, self.bank, self.branch)

    def __str__(self):
        return "{} - {} - {}".format(self.branch, self.city, self.bank)

    @property
    def bank_name(self):
        return self.bank.name


