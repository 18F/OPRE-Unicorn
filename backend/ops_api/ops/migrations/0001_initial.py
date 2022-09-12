import os

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
            ],
            options={
                "verbose_name_plural": "CANs",
            },
        ),
        migrations.CreateModel(
            name="Contract",
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
                    "cans",
                    models.ManyToManyField(related_name="contracts", to="ops.can"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ContractLineItem",
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
                    "contract",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="line_items",
                        to="ops.contract",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ContractLineItemFiscalYear",
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
                    "line_item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fiscal_years",
                        to="ops.contractlineitem",
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
            name="ContractLineItemFiscalYearPerCAN",
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
                ("funding", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "can",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="line_items_fy",
                        to="ops.can",
                    ),
                ),
                (
                    "fiscal_year",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cans",
                        to="ops.contractlineitemfiscalyear",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="can",
            name="authorizer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="authorizers",
                to="ops.fundingpartner",
            ),
        ),
        migrations.AddField(
            model_name="can",
            name="funding_source",
            field=models.ManyToManyField(to="ops.fundingsource"),
        ),
        migrations.AddField(
            model_name="can",
            name="portfolio",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="cans",
                to="ops.portfolio",
            ),
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
                    "amount_available",
                    models.DecimalField(decimal_places=2, max_digits=12),
                ),
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
                "unique_together": {("can", "fiscal_year")},
            },
        ),
    ]

    # If the old tables still exist within local Docker env or in Cloud.gov then clean them up
    # Do not run this in unit tests - sqllite does not support CASCADE
    if os.getenv("DJANGO_SETTINGS_MODULE") != "ops_api.django_config.settings.test":
        operations.append(
            migrations.RunSQL(
                [
                    "DROP TABLE IF EXISTS ops_site_can CASCADE;",
                    "DROP TABLE IF EXISTS ops_site_can_funding_source CASCADE;",
                    "DROP TABLE IF EXISTS ops_site_canfiscalyear CASCADE;",
                    "DROP TABLE IF EXISTS ops_site_canfiscalyear_can_lead CASCADE;",
                    "DROP TABLE IF EXISTS ops_site_contract CASCADE;",
                    "DROP TABLE IF EXISTS ops_site_contract_cans CASCADE;",
                    "DROP TABLE IF EXISTS ops_site_contractlineitem CASCADE;",
                    "DROP TABLE IF EXISTS ops_site_contractlineitemfiscalyear CASCADE;",
                    "DROP TABLE IF EXISTS ops_site_contractlineitemfiscalyearpercan CASCADE;",
                    "DROP TABLE IF EXISTS ops_site_fundingpartner CASCADE;",
                    "DROP TABLE IF EXISTS ops_site_fundingsource CASCADE;",
                    "DROP TABLE IF EXISTS ops_site_person CASCADE;",
                    "DROP TABLE IF EXISTS ops_site_person_roles CASCADE;",
                    "DROP TABLE IF EXISTS ops_site_portfolio CASCADE;",
                    "DROP TABLE IF EXISTS ops_site_role CASCADE;",
                ]
            )
        )
