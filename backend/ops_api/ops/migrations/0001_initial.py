# Generated by Django 4.1.1 on 2022-10-03 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Agreement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                (
                    "agreement_type",
                    models.CharField(
                        choices=[
                            ("Contract", "Contract"),
                            ("Grant", "Grant"),
                            ("Direct Allocation", "Direct Allocation"),
                            ("IAA", "Iaa"),
                            ("Miscellaneous", "Misc"),
                            (
                                "<class 'ops_api.ops.cans.models.Agreement.AgreementType.Meta'>",
                                "Meta",
                            ),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FundingPartner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("nickname", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "ops_funding_partner",
            },
        ),
        migrations.CreateModel(
            name="FundingSource",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("nickname", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "ops_funding_source",
            },
        ),
        migrations.CreateModel(
            name="Portfolio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
                ("description", models.TextField(blank=True, default="")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("In-Process", "In-Process"),
                            ("Not-Started", "Not-Started"),
                            ("Sandbox", "Sandbox"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "current_fiscal_year_funding",
                    models.DecimalField(decimal_places=2, max_digits=12),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Role Name")),
            ],
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                (
                    "division",
                    models.CharField(
                        choices=[
                            ("DCFD", "DCFD"),
                            ("DDI", "DDI"),
                            ("DEI", "DEI"),
                            ("DFS", "DFS"),
                            ("OD", "OD"),
                        ],
                        max_length=5,
                    ),
                ),
                ("roles", models.ManyToManyField(to="ops.role")),
            ],
            options={
                "verbose_name_plural": "People",
            },
        ),
        migrations.CreateModel(
            name="CAN",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.CharField(max_length=30)),
                ("description", models.CharField(max_length=100)),
                ("purpose", models.TextField(blank=True, default="")),
                ("nickname", models.CharField(max_length=30)),
                (
                    "arrangement_type",
                    models.CharField(
                        choices=[
                            ("OPRE Appropriation", "Opre Appropriation"),
                            ("Cost Share", "Cost Share"),
                            ("IAA", "Iaa"),
                            ("IDDA", "Idda"),
                            ("MOU", "Mou"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "authorizer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="authorizers",
                        to="ops.fundingpartner",
                    ),
                ),
                ("funding_source", models.ManyToManyField(to="ops.fundingsource")),
                (
                    "portfolio",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="cans",
                        to="ops.portfolio",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "CANs",
            },
        ),
        migrations.CreateModel(
            name="BudgetLineItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                ("fiscal_year", models.IntegerField()),
                ("funding", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "agreement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="ops.agreement"
                    ),
                ),
                (
                    "can",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="ops.can"
                    ),
                ),
            ],
            options={
                "db_table": "ops_budget_line_item",
            },
        ),
        migrations.AddField(
            model_name="agreement",
            name="cans",
            field=models.ManyToManyField(related_name="contracts", to="ops.can"),
        ),
        migrations.CreateModel(
            name="CANFiscalYear",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fiscal_year", models.IntegerField()),
                (
                    "total_fiscal_year_funding",
                    models.DecimalField(decimal_places=2, max_digits=12),
                ),
                (
                    "potential_additional_funding",
                    models.DecimalField(decimal_places=2, max_digits=12),
                ),
                ("notes", models.TextField(blank=True, default="")),
                (
                    "can",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="ops.can"
                    ),
                ),
                ("can_lead", models.ManyToManyField(to="ops.person")),
            ],
            options={
                "verbose_name_plural": "CANs (fiscal year)",
                "db_table": "ops_can_fiscal_year",
                "unique_together": {("can", "fiscal_year")},
            },
        ),
    ]
