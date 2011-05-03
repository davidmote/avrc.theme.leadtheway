from five import grok
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from plone.app.layout.viewlets.interfaces import IPortalHeader
from zope.interface import Interface
from zope.app.component.hooks import getSite

# Apply on everything.
# Use templates directory to search for templates.
grok.templatedir('templates')

class SlideshowViewlet(grok.Viewlet):
    grok.name('leadtheway.SlideshowViewlet')
    grok.context(Interface)
    grok.require('zope2.View')
    grok.viewletmanager(IPortalHeader)

    
    def slideshowContainer(self):
        site = getSite()
        try:
            return site.restrictedTraverse('slideshow')
        except KeyError:
            return None

    def slideshowImages(self):
        slideshow_container = self.slideshowContainer()
        if slideshow_container is not None:
            imageBrains = slideshow_container.getFolderContents({'portal_type':'Image'})
        else:
            imageBrains = []
        return imageBrains