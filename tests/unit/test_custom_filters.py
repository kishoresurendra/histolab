# -*- coding: utf-8 -*-
from histolab.slide import Slide
from histolab.tiler import GridTiler
from histolab.masks import TissueMask
import histolab.filters.image_filters as imf
import histolab.filters.morphological_filters as mof
from histolab.data import ovarian_tissue


def extractTiles(all_tissue_mask , slidetox):

    slidetox.locate_mask(all_tissue_mask).show()

    random_tiles_extractor = GridTiler(
                tile_size=(64, 64),
                level=0,
                check_tissue=True,
                tissue_percent=90.0,
                pixel_overlap=0,
                prefix="tile",
                suffix=".png"
            )


    random_tiles_extractor.extract(slidetox,all_tissue_mask)

#Select an ovarian tissue slide
ovarian_svs, ovarian_path = ovarian_tissue()

#Set a custom filters mask instance : No dilation and min size set for small objects
all_tissue_custom_mask = TissueMask(
    imf.RgbToGrayscale(),
    imf.OtsuThreshold(),
    mof.RemoveSmallObjects(min_size=500),
    mof.RemoveSmallHoles()
 )

#Set a default mask instance
all_tissue_default_mask = TissueMask()

#Set an output tile path for custom and default filters separately
custom_tile_path = '/CustomOutput/'
default_tile_path = '/DefaultOutput/'

#Create slide instance for custom and default filters separately
slidetox_custom = Slide(ovarian_path,custom_tile_path)
slidetox_default = Slide(ovarian_path,default_tile_path)

#Extract tiles for both scenarios
extractTiles(all_tissue_custom_mask , slidetox_custom)
extractTiles(all_tissue_default_mask , slidetox_default)
