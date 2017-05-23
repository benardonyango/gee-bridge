# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_gdal_array', [dirname(__file__)])
        except ImportError:
            import _gdal_array
            return _gdal_array
        if fp is not None:
            try:
                _mod = imp.load_module('_gdal_array', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _gdal_array = swig_import_helper()
    del swig_import_helper
else:
    import _gdal_array
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


from osgeo import gdal
class VirtualMem(_object):
    """Proxy of C++ CPLVirtualMemShadow class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VirtualMem, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VirtualMem, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _gdal_array.delete_VirtualMem
    __del__ = lambda self : None;
    def GetAddr(self):
        """GetAddr(VirtualMem self)"""
        return _gdal_array.VirtualMem_GetAddr(self)

    def Pin(self, start_offset=0, nsize=0, bWriteOp=0):
        """
        Pin(VirtualMem self, size_t start_offset=0, size_t nsize=0, int bWriteOp=0)
        Pin(VirtualMem self, size_t start_offset=0, size_t nsize=0)
        Pin(VirtualMem self, size_t start_offset=0)
        Pin(VirtualMem self)
        """
        return _gdal_array.VirtualMem_Pin(self, start_offset, nsize, bWriteOp)

VirtualMem_swigregister = _gdal_array.VirtualMem_swigregister
VirtualMem_swigregister(VirtualMem)


def TermProgress_nocb(*args, **kwargs):
  """TermProgress_nocb(double dfProgress, char const * pszMessage=None, void * pData=None) -> int"""
  return _gdal_array.TermProgress_nocb(*args, **kwargs)
TermProgress = _gdal_array.TermProgress

def OpenNumPyArray(*args):
  """OpenNumPyArray(PyArrayObject * psArray) -> Dataset"""
  return _gdal_array.OpenNumPyArray(*args)
OpenNumPyArray = _gdal_array.OpenNumPyArray

def GetArrayFilename(*args):
  """GetArrayFilename(PyArrayObject * psArray) -> retStringAndCPLFree *"""
  return _gdal_array.GetArrayFilename(*args)
GetArrayFilename = _gdal_array.GetArrayFilename

def BandRasterIONumPy(*args, **kwargs):
  """
    BandRasterIONumPy(Band band, int bWrite, double xoff, double yoff, double xsize, double ysize, PyArrayObject * psArray, 
        int buf_type, GDALRIOResampleAlg resample_alg, GDALProgressFunc callback=0, 
        void * callback_data=None) -> CPLErr
    """
  return _gdal_array.BandRasterIONumPy(*args, **kwargs)
BandRasterIONumPy = _gdal_array.BandRasterIONumPy

def DatasetIONumPy(*args, **kwargs):
  """
    DatasetIONumPy(Dataset ds, int bWrite, int xoff, int yoff, int xsize, int ysize, PyArrayObject * psArray, 
        int buf_type, GDALRIOResampleAlg resample_alg, GDALProgressFunc callback=0, 
        void * callback_data=None) -> CPLErr
    """
  return _gdal_array.DatasetIONumPy(*args, **kwargs)
DatasetIONumPy = _gdal_array.DatasetIONumPy

def VirtualMemGetArray(*args):
  """VirtualMemGetArray(VirtualMem virtualmem)"""
  return _gdal_array.VirtualMemGetArray(*args)
VirtualMemGetArray = _gdal_array.VirtualMemGetArray

def RATValuesIONumPyWrite(*args, **kwargs):
  """RATValuesIONumPyWrite(RasterAttributeTable poRAT, int nField, int nStart, PyArrayObject * psArray) -> CPLErr"""
  return _gdal_array.RATValuesIONumPyWrite(*args, **kwargs)
RATValuesIONumPyWrite = _gdal_array.RATValuesIONumPyWrite

def RATValuesIONumPyRead(*args, **kwargs):
  """RATValuesIONumPyRead(RasterAttributeTable poRAT, int nField, int nStart, int nLength) -> PyObject *"""
  return _gdal_array.RATValuesIONumPyRead(*args, **kwargs)
RATValuesIONumPyRead = _gdal_array.RATValuesIONumPyRead
import numpy
import _gdal_array

from osgeo import gdalconst
from osgeo import gdal
gdal.AllRegister()

codes = {   gdalconst.GDT_Byte      :   numpy.uint8,
            gdalconst.GDT_UInt16    :   numpy.uint16,
            gdalconst.GDT_Int16     :   numpy.int16,
            gdalconst.GDT_UInt32    :   numpy.uint32,
            gdalconst.GDT_Int32     :   numpy.int32,
            gdalconst.GDT_Float32   :   numpy.float32,
            gdalconst.GDT_Float64   :   numpy.float64,
            gdalconst.GDT_CInt16    :   numpy.complex64,
            gdalconst.GDT_CInt32    :   numpy.complex64,
            gdalconst.GDT_CFloat32  :   numpy.complex64,
            gdalconst.GDT_CFloat64  :   numpy.complex128
        }

def OpenArray( array, prototype_ds = None ):

    ds = OpenNumPyArray( array )

    if ds is not None and prototype_ds is not None:
        if type(prototype_ds).__name__ == 'str':
            prototype_ds = gdal.Open( prototype_ds )
        if prototype_ds is not None:
            CopyDatasetInfo( prototype_ds, ds )

    return ds


def flip_code(code):
    if isinstance(code, (numpy.dtype,type)):
        # since several things map to complex64 we must carefully select
        # the opposite that is an exact match (ticket 1518)
        if code == numpy.int8:
            return gdalconst.GDT_Byte
        if code == numpy.complex64:
            return gdalconst.GDT_CFloat32

        for key, value in codes.items():
            if value == code:
                return key
        return None
    else:
        try:
            return codes[code]
        except KeyError:
            return None

def NumericTypeCodeToGDALTypeCode(numeric_type):
    if not isinstance(numeric_type, (numpy.dtype,type)):
        raise TypeError("Input must be a type")
    return flip_code(numeric_type)

def GDALTypeCodeToNumericTypeCode(gdal_code):
    return flip_code(gdal_code)

def LoadFile( filename, xoff=0, yoff=0, xsize=None, ysize=None,
              buf_xsize=None, buf_ysize=None, buf_type=None,
              resample_alg = gdal.GRIORA_NearestNeighbour,
              callback=None, callback_data=None ):
    ds = gdal.Open( filename )
    if ds is None:
        raise ValueError("Can't open "+filename+"\n\n"+gdal.GetLastErrorMsg())

    return DatasetReadAsArray( ds, xoff, yoff, xsize, ysize,
                               buf_xsize=buf_xsize, buf_ysize=buf_ysize, buf_type=buf_type,
                               resample_alg=resample_alg,
                               callback = callback, callback_data = callback_data )

def SaveArray( src_array, filename, format = "GTiff", prototype = None ):
    driver = gdal.GetDriverByName( format )
    if driver is None:
        raise ValueError("Can't find driver "+format)

    return driver.CreateCopy( filename, OpenArray(src_array,prototype) )


def DatasetReadAsArray( ds, xoff=0, yoff=0, win_xsize=None, win_ysize=None, buf_obj=None,
                        buf_xsize = None, buf_ysize = None, buf_type = None,
                        resample_alg = gdal.GRIORA_NearestNeighbour,
                        callback=None, callback_data=None ):
    """Pure python implementation of reading a chunk of a GDAL file
    into a numpy array.  Used by the gdal.Dataset.ReadAsArray method."""

    if win_xsize is None:
        win_xsize = ds.RasterXSize
    if win_ysize is None:
        win_ysize = ds.RasterYSize

    if ds.RasterCount == 0:
        return None

    if ds.RasterCount == 1:
        return BandReadAsArray( ds.GetRasterBand(1), xoff, yoff, win_xsize, win_ysize,
                                buf_xsize = buf_xsize, buf_ysize = buf_ysize, buf_type = buf_type,
                                buf_obj = buf_obj,
                                resample_alg = resample_alg,
                                callback = callback,
                                callback_data = callback_data )

    if buf_obj is None:
        if buf_xsize is None:
            buf_xsize = win_xsize
        if buf_ysize is None:
            buf_ysize = win_ysize
        if buf_type is None:
            buf_type = ds.GetRasterBand(1).DataType
            for band_index in range(2,ds.RasterCount+1):
                if buf_type != ds.GetRasterBand(band_index).DataType:
                    buf_type = gdalconst.GDT_Float32

        typecode = GDALTypeCodeToNumericTypeCode( buf_type )
        if typecode == None:
            buf_type = gdalconst.GDT_Float32
            typecode = numpy.float32
        if buf_type == gdalconst.GDT_Byte and ds.GetRasterBand(1).GetMetadataItem('PIXELTYPE', 'IMAGE_STRUCTURE') == 'SIGNEDBYTE':
            typecode = numpy.int8
        buf_obj = numpy.empty([ds.RasterCount, buf_ysize,buf_xsize], dtype = typecode)

    else:
        if len(buf_obj.shape) != 3:
            raise ValueError('Array should have 3 dimensions')

        shape_buf_xsize = buf_obj.shape[2]
        shape_buf_ysize = buf_obj.shape[1]
        if buf_xsize is not None and buf_xsize != shape_buf_xsize:
            raise ValueError('Specified buf_xsize not consistent with array shape')
        if buf_ysize is not None and buf_ysize != shape_buf_ysize:
            raise ValueError('Specified buf_ysize not consistent with array shape')
        if buf_obj.shape[0] != ds.RasterCount:
            raise ValueError('Array should have space for %d bands' % ds.RasterCount)

        datatype = NumericTypeCodeToGDALTypeCode( buf_obj.dtype.type )
        if not datatype:
            raise ValueError("array does not have corresponding GDAL data type")
        if buf_type is not None and buf_type != datatype:
            raise ValueError("Specified buf_type not consistent with array type")
        buf_type = datatype

    if DatasetIONumPy( ds, 0, xoff, yoff, win_xsize, win_ysize,
                       buf_obj, buf_type, resample_alg, callback, callback_data ) != 0:
        return None

    return buf_obj

def BandReadAsArray( band, xoff = 0, yoff = 0, win_xsize = None, win_ysize = None,
                     buf_xsize=None, buf_ysize=None, buf_type=None, buf_obj=None,
                     resample_alg = gdal.GRIORA_NearestNeighbour,
                     callback=None, callback_data=None):
    """Pure python implementation of reading a chunk of a GDAL file
    into a numpy array.  Used by the gdal.Band.ReadAsArray method."""

    if win_xsize is None:
        win_xsize = band.XSize
    if win_ysize is None:
        win_ysize = band.YSize

    if buf_obj is None:
        if buf_xsize is None:
            buf_xsize = win_xsize
        if buf_ysize is None:
            buf_ysize = win_ysize
        if buf_type is None:
            buf_type = band.DataType

        typecode = GDALTypeCodeToNumericTypeCode( buf_type )
        if typecode == None:
            buf_type = gdalconst.GDT_Float32
            typecode = numpy.float32
        else:
            buf_type = NumericTypeCodeToGDALTypeCode( typecode )

        if buf_type == gdalconst.GDT_Byte and band.GetMetadataItem('PIXELTYPE', 'IMAGE_STRUCTURE') == 'SIGNEDBYTE':
            typecode = numpy.int8
        buf_obj = numpy.empty([buf_ysize,buf_xsize], dtype = typecode)

    else:
        if len(buf_obj.shape) == 2:
            shape_buf_xsize = buf_obj.shape[1]
            shape_buf_ysize = buf_obj.shape[0]
        else:
            shape_buf_xsize = buf_obj.shape[2]
            shape_buf_ysize = buf_obj.shape[1]
        if buf_xsize is not None and buf_xsize != shape_buf_xsize:
            raise ValueError('Specified buf_xsize not consistent with array shape')
        if buf_ysize is not None and buf_ysize != shape_buf_ysize:
            raise ValueError('Specified buf_ysize not consistent with array shape')

        datatype = NumericTypeCodeToGDALTypeCode( buf_obj.dtype.type )
        if not datatype:
            raise ValueError("array does not have corresponding GDAL data type")
        if buf_type is not None and buf_type != datatype:
            raise ValueError("Specified buf_type not consistent with array type")
        buf_type = datatype

    if BandRasterIONumPy( band, 0, xoff, yoff, win_xsize, win_ysize,
                          buf_obj, buf_type, resample_alg, callback, callback_data ) != 0:
        return None

    return buf_obj

def BandWriteArray( band, array, xoff=0, yoff=0,
                    resample_alg = gdal.GRIORA_NearestNeighbour,
                    callback=None, callback_data=None ):
    """Pure python implementation of writing a chunk of a GDAL file
    from a numpy array.  Used by the gdal.Band.WriteArray method."""

    if array is None or len(array.shape) != 2:
        raise ValueError("expected array of dim 2")

    xsize = array.shape[1]
    ysize = array.shape[0]

    if xsize + xoff > band.XSize or ysize + yoff > band.YSize:
        raise ValueError("array larger than output file, or offset off edge")

    datatype = NumericTypeCodeToGDALTypeCode( array.dtype.type )

    # if we receive some odd type, like int64, try casting to a very
    # generic type we do support (#2285)
    if not datatype:
        gdal.Debug( 'gdal_array', 'force array to float64' )
        array = array.astype( numpy.float64 )
        datatype = NumericTypeCodeToGDALTypeCode( array.dtype.type )

    if not datatype:
        raise ValueError("array does not have corresponding GDAL data type")

    return BandRasterIONumPy( band, 1, xoff, yoff, xsize, ysize,
                                array, datatype, resample_alg, callback, callback_data )

def RATWriteArray(rat, array, field, start=0):
    """
    Pure Python implementation of writing a chunk of the RAT
    from a numpy array. Type of array is coerced to one of the types
    (int, double, string) supported. Called from RasterAttributeTable.WriteArray
    """
    if array is None:
        raise ValueError("Expected array of dim 1")

    # if not the array type convert it to handle lists etc
    if not isinstance(array, numpy.ndarray):
        array = numpy.array(array)

    if array.ndim != 1:
        raise ValueError("Expected array of dim 1")

    if (start + array.size) > rat.GetRowCount():
        raise ValueError("Array too big to fit into RAT from start position")

    if numpy.issubdtype(array.dtype, numpy.integer):
        # is some type of integer - coerce to standard int
        # TODO: must check this is fine on all platforms
        # confusingly numpy.int 64 bit even if native type 32 bit
        array = array.astype(numpy.int32)
    elif numpy.issubdtype(array.dtype, numpy.floating):
        # is some type of floating point - coerce to double
        array = array.astype(numpy.double)
    elif numpy.issubdtype(array.dtype, numpy.character):
        # cast away any kind of Unicode etc
        array = array.astype(numpy.character)
    else:
        raise ValueError("Array not of a supported type (integer, double or string)")

    return RATValuesIONumPyWrite(rat, field, start, array)

def RATReadArray(rat, field, start=0, length=None):
    """
    Pure Python implementation of reading a chunk of the RAT
    into a numpy array. Called from RasterAttributeTable.ReadAsArray
    """
    if length is None:
        length = rat.GetRowCount() - start

    return RATValuesIONumPyRead(rat, field, start, length)

def CopyDatasetInfo( src, dst, xoff=0, yoff=0 ):
    """
    Copy georeferencing information and metadata from one dataset to another.
    src: input dataset
    dst: output dataset - It can be a ROI -
    xoff, yoff:  dst's offset with respect to src in pixel/line.

    Notes: Destination dataset must have update access.  Certain formats
           do not support creation of geotransforms and/or gcps.

    """

    dst.SetMetadata( src.GetMetadata() )



    #Check for geo transform
    gt = src.GetGeoTransform()
    if gt != (0,1,0,0,0,1):
        dst.SetProjection( src.GetProjectionRef() )

        if (xoff == 0) and (yoff == 0):
            dst.SetGeoTransform( gt  )
        else:
            ngt = [gt[0],gt[1],gt[2],gt[3],gt[4],gt[5]]
            ngt[0] = gt[0] + xoff*gt[1] + yoff*gt[2];
            ngt[3] = gt[3] + xoff*gt[4] + yoff*gt[5];
            dst.SetGeoTransform( ( ngt[0], ngt[1], ngt[2], ngt[3], ngt[4], ngt[5] ) )

    #Check for GCPs
    elif src.GetGCPCount() > 0:

        if (xoff == 0) and (yoff == 0):
            dst.SetGCPs( src.GetGCPs(), src.GetGCPProjection() )
        else:
            gcps = src.GetGCPs()
            #Shift gcps
            new_gcps = []
            for gcp in gcps:
                ngcp = gdal.GCP()
                ngcp.GCPX = gcp.GCPX
                ngcp.GCPY = gcp.GCPY
                ngcp.GCPZ = gcp.GCPZ
                ngcp.GCPPixel = gcp.GCPPixel - xoff
                ngcp.GCPLine = gcp.GCPLine - yoff
                ngcp.Info = gcp.Info
                ngcp.Id = gcp.Id
                new_gcps.append(ngcp)

            try:
                dst.SetGCPs( new_gcps , src.GetGCPProjection() )
            except:
                print ("Failed to set GCPs")
                return

    return

# This file is compatible with both classic and new-style classes.


