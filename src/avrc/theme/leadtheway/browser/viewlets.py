from five import grok
from plone.app.layout.viewlets.interfaces import IPortalHeader
from zope.interface import Interface
from zope.app.component.hooks import getSite
import random
from avrc.theme.leadtheway.interfaces import ILeadthewayTheme
from plone.memoize import view

# Apply on everything.
# Use templates directory to search for templates.
grok.templatedir('templates')

def _mosaic_cachekey(method, self, brain):
    return (brain.getPath(), brain.modified)

class SlideshowViewlet(grok.Viewlet):
    grok.name('leadtheway.SlideshowViewlet')
    grok.context(Interface)
    grok.require('zope2.View')
    grok.layer(ILeadthewayTheme)
    grok.viewletmanager(IPortalHeader)


    def slideshowContainer(self):
        site = getSite()
        try:
            return site.restrictedTraverse('slideshow')
        except KeyError:
            return None

    def isHomePage(self):
        context_state = self.context.restrictedTraverse('@@plone_context_state')
        return context_state.is_portal_root() and context_state.is_view_template()
        
    def slideshowImages(self):
        slideshow_container = self.slideshowContainer()
        if slideshow_container is not None:
            imageBrains = list(slideshow_container.getFolderContents({'portal_type':'Image'}))
            random.shuffle(imageBrains)
        else:
            imageBrains = []
        return imageBrains
        
    @view.memoize
    def mosaicImages(self):
        theme_path = '++theme++avrc.theme.leadtheway/theme-mosaic'
        theme_dir = self.context.restrictedTraverse(theme_path)
        rslts = []
        for image in theme_dir.listDirectory():
            rslts.append(theme_path + '/' + image)
        rslts.sort()
        return rslts