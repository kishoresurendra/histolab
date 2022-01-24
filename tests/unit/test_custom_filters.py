# -*- coding: utf-8 -*-
from histolab.slide import Slide
from histolab.masks import TissueMask
import histolab.filters.image_filters as imf
import histolab.filters.morphological_filters as mof
from histolab.data import ovarian_tissue


def fetch_masked_image(all_tissue_mask , slidetox):
    mask = slidetox.locate_mask(all_tissue_mask)
    return mask

#Select an ovarian tissue slide
ovarian_svs, ovarian_path = ovarian_tissue()


#Set a custom filters mask instance : Return only the bright image spots
all_tissue_custom_mask = TissueMask(
    imf.RgbToGrayscale(),
    imf.OtsuThreshold(),
    mof.WhiteTopHat()
 )

#The default settings lead to selection of mainly the tissue areas within a WSI
all_tissue_default_mask = TissueMask()

#Set an output tile path for custom and default filters separately
custom_tile_path = 'CustomOutput'
default_tile_path = 'DefaultOutput'

#Create slide instance for custom and default filters separately
slidetox_custom = Slide(ovarian_path,custom_tile_path)
slidetox_default = Slide(ovarian_path,default_tile_path)

#Fetch the resulting image after applying tissue masks
custom_mask_img = fetch_masked_image(all_tissue_custom_mask , slidetox_custom)
default_mask_img = fetch_masked_image(all_tissue_default_mask , slidetox_default)
