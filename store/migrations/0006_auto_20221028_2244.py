# Generated by Django 4.1.2 on 2022-10-28 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_customer_store_custo_first_n_a7e990_idx_and_more'),
    ]

    operations = [
        migrations.RunSQL("""
        INSERT INTO store_collection (title)
        VALUES ('collection1')
        """, """
        DELETE FROM store_collection 
        WHERE title='collection1'
        """)
    ]