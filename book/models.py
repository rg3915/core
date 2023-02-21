from django.db import models
from wagtail.models import Orderable
from modelcluster.models import ClusterableModel
from location.models import Location
from core.choices import LANGUAGE
from django.utils.translation import gettext as _

from core.models import CommonControlField
from institution.models import Institution

from book.forms import BookModelForm, ChapterModelForm


class Book(CommonControlField, ClusterableModel):
    """
        A class to represent a book model designed in the SciELO context.

        Attributes
        ----------
        location = Country, State and City model
        institution = the publisher that in general is a institution
        isbn = the International Standard Book Number of the book
        eisbn = the electronic International Standard Book Number of the book
        language = the language with a closed list 
        synopsis = a short description of the contents
        title = the title of the book
        year = the year with max_length = 4
        doi = the Digital Object Identifier of the book

        CommonControlField:
            created = date of creation the data in this database
            updated = date of the latest update
            creator = the user create the data
            updated_by = the user last update the data.

        Methods
        -------
        TODO
    """

    location = models.ForeignKey(Location, verbose_name=_("Localization"), null=True, blank=True, on_delete=models.SET_NULL)
    institution = models.ForeignKey(Institution, verbose_name=_("Publisher"), null=True, blank=True, on_delete=models.SET_NULL)

    isbn = models.CharField("ISBN", max_length=13, null=True, blank=True)
    eisbn = models.CharField(_("Electronic ISBN"), max_length=13, null=True, blank=True)
    language = models.CharField(_("Language"), max_length=256, choices=LANGUAGE, null=True, blank=True)
    synopsis = models.TextField(_("Synopsis"), null=True, blank=True)
    title = models.CharField(_("Title"), max_length=256, null=True, blank=True)
    year = models.IntegerField(_("Year"), null=True, blank=True)
    doi = models.CharField("DOI", max_length=20, null=True, blank=True)
    
    class Meta:
        verbose_name = _('SciELO Book')
        verbose_name_plural = _('SciELO Books')
        indexes = [
            models.Index(fields=['isbn', ]),
            models.Index(fields=['title', ]),
            models.Index(fields=['synopsis', ]),
            models.Index(fields=['doi', ]),
        ]

    def __unicode__(self):
        return u'%s' % self.title or ''

    def __str__(self):
        return u'%s' % self.title or ''

    base_form_class = BookModelForm



class Chapter(Orderable, CommonControlField):
    """
        A class to represent a part of book (chapter) model designed in the SciELO context.

        Attributes
        ----------
        title = the title of the chapter
        language = the language with a closed list 
        publication_date = the publication date 

        Methods
        -------
        TODO
    """  
    title = models.CharField(_("Title"), max_length=256, null=True, blank=True)
    language = models.CharField(_("Language"), max_length=256, choices=LANGUAGE, null=True, blank=True)
    publication_date = models.CharField(_("Data de publicação"), max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = _('Chapter')
        verbose_name_plural = _('Chapters')
        indexes = [
            models.Index(fields=['title', ]),
            models.Index(fields=['language', ]),
            models.Index(fields=['publication_date', ]),
        ]

    def __unicode__(self):
        return u'%s' % self.title or ''

    def __str__(self):
        return u'%s' % self.title or ''

    base_form_class = ChapterModelForm