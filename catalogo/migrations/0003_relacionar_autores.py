from django.db import migrations


def relacionar_autores(apps, schema_editor):
    Libro = apps.get_model('catalogo', 'Libro')
    Autor = apps.get_model('catalogo', 'Autor')
    base_datos = schema_editor.connection.alias

    for libro in Libro.objects.using(base_datos).all():
        if libro.autor:
            autor, creado = Autor.objects.using(base_datos).get_or_create(nombre=libro.autor)
            libro.autores.add(autor)


class Migration(migrations.Migration):
    dependencies = [
        ('catalogo', '0002_autor_editorial_libro_estado_libro_precio_and_more'),
    ]

    operations = [
        migrations.RunPython(relacionar_autores, migrations.RunPython.noop),
    ]
