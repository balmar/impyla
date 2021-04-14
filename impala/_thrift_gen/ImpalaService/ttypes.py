#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import impala._thrift_gen.ExecStats.ttypes
import impala._thrift_gen.Status.ttypes
import impala._thrift_gen.Types.ttypes
import impala._thrift_gen.beeswax.ttypes
import impala._thrift_gen.TCLIService.ttypes
import impala._thrift_gen.RuntimeProfile.ttypes

from thrift.transport import TTransport
all_structs = []


class TImpalaQueryOptions(object):
    ABORT_ON_ERROR = 0
    MAX_ERRORS = 1
    DISABLE_CODEGEN = 2
    BATCH_SIZE = 3
    MEM_LIMIT = 4
    NUM_NODES = 5
    MAX_SCAN_RANGE_LENGTH = 6
    MAX_IO_BUFFERS = 7
    NUM_SCANNER_THREADS = 8
    ALLOW_UNSUPPORTED_FORMATS = 9
    DEFAULT_ORDER_BY_LIMIT = 10
    DEBUG_ACTION = 11
    ABORT_ON_DEFAULT_LIMIT_EXCEEDED = 12
    COMPRESSION_CODEC = 13
    SEQ_COMPRESSION_MODE = 14
    HBASE_CACHING = 15
    HBASE_CACHE_BLOCKS = 16
    PARQUET_FILE_SIZE = 17
    EXPLAIN_LEVEL = 18
    SYNC_DDL = 19
    REQUEST_POOL = 20
    V_CPU_CORES = 21
    RESERVATION_REQUEST_TIMEOUT = 22
    DISABLE_CACHED_READS = 23
    DISABLE_OUTERMOST_TOPN = 24
    RM_INITIAL_MEM = 25
    QUERY_TIMEOUT_S = 26
    BUFFER_POOL_LIMIT = 27
    APPX_COUNT_DISTINCT = 28
    DISABLE_UNSAFE_SPILLS = 29
    EXEC_SINGLE_NODE_ROWS_THRESHOLD = 30
    OPTIMIZE_PARTITION_KEY_SCANS = 31
    REPLICA_PREFERENCE = 32
    SCHEDULE_RANDOM_REPLICA = 33
    SCAN_NODE_CODEGEN_THRESHOLD = 34
    DISABLE_STREAMING_PREAGGREGATIONS = 35
    RUNTIME_FILTER_MODE = 36
    RUNTIME_BLOOM_FILTER_SIZE = 37
    RUNTIME_FILTER_WAIT_TIME_MS = 38
    DISABLE_ROW_RUNTIME_FILTERING = 39
    MAX_NUM_RUNTIME_FILTERS = 40
    PARQUET_ANNOTATE_STRINGS_UTF8 = 41
    PARQUET_FALLBACK_SCHEMA_RESOLUTION = 42
    MT_DOP = 43
    S3_SKIP_INSERT_STAGING = 44
    RUNTIME_FILTER_MAX_SIZE = 45
    RUNTIME_FILTER_MIN_SIZE = 46
    PREFETCH_MODE = 47
    STRICT_MODE = 48
    SCRATCH_LIMIT = 49
    ENABLE_EXPR_REWRITES = 50
    DECIMAL_V2 = 51
    PARQUET_DICTIONARY_FILTERING = 52
    PARQUET_ARRAY_RESOLUTION = 53
    PARQUET_READ_STATISTICS = 54
    DEFAULT_JOIN_DISTRIBUTION_MODE = 55
    DISABLE_CODEGEN_ROWS_THRESHOLD = 56
    DEFAULT_SPILLABLE_BUFFER_SIZE = 57
    MIN_SPILLABLE_BUFFER_SIZE = 58
    MAX_ROW_SIZE = 59
    IDLE_SESSION_TIMEOUT = 60
    COMPUTE_STATS_MIN_SAMPLE_SIZE = 61
    EXEC_TIME_LIMIT_S = 62
    SHUFFLE_DISTINCT_EXPRS = 63
    MAX_MEM_ESTIMATE_FOR_ADMISSION = 64
    THREAD_RESERVATION_LIMIT = 65
    THREAD_RESERVATION_AGGREGATE_LIMIT = 66
    KUDU_READ_MODE = 67
    ALLOW_ERASURE_CODED_FILES = 68
    TIMEZONE = 69
    SCAN_BYTES_LIMIT = 70
    CPU_LIMIT_S = 71
    TOPN_BYTES_LIMIT = 72
    CLIENT_IDENTIFIER = 73
    RESOURCE_TRACE_RATIO = 74
    NUM_REMOTE_EXECUTOR_CANDIDATES = 75
    NUM_ROWS_PRODUCED_LIMIT = 76
    PLANNER_TESTCASE_MODE = 77

    _VALUES_TO_NAMES = {
        0: "ABORT_ON_ERROR",
        1: "MAX_ERRORS",
        2: "DISABLE_CODEGEN",
        3: "BATCH_SIZE",
        4: "MEM_LIMIT",
        5: "NUM_NODES",
        6: "MAX_SCAN_RANGE_LENGTH",
        7: "MAX_IO_BUFFERS",
        8: "NUM_SCANNER_THREADS",
        9: "ALLOW_UNSUPPORTED_FORMATS",
        10: "DEFAULT_ORDER_BY_LIMIT",
        11: "DEBUG_ACTION",
        12: "ABORT_ON_DEFAULT_LIMIT_EXCEEDED",
        13: "COMPRESSION_CODEC",
        14: "SEQ_COMPRESSION_MODE",
        15: "HBASE_CACHING",
        16: "HBASE_CACHE_BLOCKS",
        17: "PARQUET_FILE_SIZE",
        18: "EXPLAIN_LEVEL",
        19: "SYNC_DDL",
        20: "REQUEST_POOL",
        21: "V_CPU_CORES",
        22: "RESERVATION_REQUEST_TIMEOUT",
        23: "DISABLE_CACHED_READS",
        24: "DISABLE_OUTERMOST_TOPN",
        25: "RM_INITIAL_MEM",
        26: "QUERY_TIMEOUT_S",
        27: "BUFFER_POOL_LIMIT",
        28: "APPX_COUNT_DISTINCT",
        29: "DISABLE_UNSAFE_SPILLS",
        30: "EXEC_SINGLE_NODE_ROWS_THRESHOLD",
        31: "OPTIMIZE_PARTITION_KEY_SCANS",
        32: "REPLICA_PREFERENCE",
        33: "SCHEDULE_RANDOM_REPLICA",
        34: "SCAN_NODE_CODEGEN_THRESHOLD",
        35: "DISABLE_STREAMING_PREAGGREGATIONS",
        36: "RUNTIME_FILTER_MODE",
        37: "RUNTIME_BLOOM_FILTER_SIZE",
        38: "RUNTIME_FILTER_WAIT_TIME_MS",
        39: "DISABLE_ROW_RUNTIME_FILTERING",
        40: "MAX_NUM_RUNTIME_FILTERS",
        41: "PARQUET_ANNOTATE_STRINGS_UTF8",
        42: "PARQUET_FALLBACK_SCHEMA_RESOLUTION",
        43: "MT_DOP",
        44: "S3_SKIP_INSERT_STAGING",
        45: "RUNTIME_FILTER_MAX_SIZE",
        46: "RUNTIME_FILTER_MIN_SIZE",
        47: "PREFETCH_MODE",
        48: "STRICT_MODE",
        49: "SCRATCH_LIMIT",
        50: "ENABLE_EXPR_REWRITES",
        51: "DECIMAL_V2",
        52: "PARQUET_DICTIONARY_FILTERING",
        53: "PARQUET_ARRAY_RESOLUTION",
        54: "PARQUET_READ_STATISTICS",
        55: "DEFAULT_JOIN_DISTRIBUTION_MODE",
        56: "DISABLE_CODEGEN_ROWS_THRESHOLD",
        57: "DEFAULT_SPILLABLE_BUFFER_SIZE",
        58: "MIN_SPILLABLE_BUFFER_SIZE",
        59: "MAX_ROW_SIZE",
        60: "IDLE_SESSION_TIMEOUT",
        61: "COMPUTE_STATS_MIN_SAMPLE_SIZE",
        62: "EXEC_TIME_LIMIT_S",
        63: "SHUFFLE_DISTINCT_EXPRS",
        64: "MAX_MEM_ESTIMATE_FOR_ADMISSION",
        65: "THREAD_RESERVATION_LIMIT",
        66: "THREAD_RESERVATION_AGGREGATE_LIMIT",
        67: "KUDU_READ_MODE",
        68: "ALLOW_ERASURE_CODED_FILES",
        69: "TIMEZONE",
        70: "SCAN_BYTES_LIMIT",
        71: "CPU_LIMIT_S",
        72: "TOPN_BYTES_LIMIT",
        73: "CLIENT_IDENTIFIER",
        74: "RESOURCE_TRACE_RATIO",
        75: "NUM_REMOTE_EXECUTOR_CANDIDATES",
        76: "NUM_ROWS_PRODUCED_LIMIT",
        77: "PLANNER_TESTCASE_MODE",
    }

    _NAMES_TO_VALUES = {
        "ABORT_ON_ERROR": 0,
        "MAX_ERRORS": 1,
        "DISABLE_CODEGEN": 2,
        "BATCH_SIZE": 3,
        "MEM_LIMIT": 4,
        "NUM_NODES": 5,
        "MAX_SCAN_RANGE_LENGTH": 6,
        "MAX_IO_BUFFERS": 7,
        "NUM_SCANNER_THREADS": 8,
        "ALLOW_UNSUPPORTED_FORMATS": 9,
        "DEFAULT_ORDER_BY_LIMIT": 10,
        "DEBUG_ACTION": 11,
        "ABORT_ON_DEFAULT_LIMIT_EXCEEDED": 12,
        "COMPRESSION_CODEC": 13,
        "SEQ_COMPRESSION_MODE": 14,
        "HBASE_CACHING": 15,
        "HBASE_CACHE_BLOCKS": 16,
        "PARQUET_FILE_SIZE": 17,
        "EXPLAIN_LEVEL": 18,
        "SYNC_DDL": 19,
        "REQUEST_POOL": 20,
        "V_CPU_CORES": 21,
        "RESERVATION_REQUEST_TIMEOUT": 22,
        "DISABLE_CACHED_READS": 23,
        "DISABLE_OUTERMOST_TOPN": 24,
        "RM_INITIAL_MEM": 25,
        "QUERY_TIMEOUT_S": 26,
        "BUFFER_POOL_LIMIT": 27,
        "APPX_COUNT_DISTINCT": 28,
        "DISABLE_UNSAFE_SPILLS": 29,
        "EXEC_SINGLE_NODE_ROWS_THRESHOLD": 30,
        "OPTIMIZE_PARTITION_KEY_SCANS": 31,
        "REPLICA_PREFERENCE": 32,
        "SCHEDULE_RANDOM_REPLICA": 33,
        "SCAN_NODE_CODEGEN_THRESHOLD": 34,
        "DISABLE_STREAMING_PREAGGREGATIONS": 35,
        "RUNTIME_FILTER_MODE": 36,
        "RUNTIME_BLOOM_FILTER_SIZE": 37,
        "RUNTIME_FILTER_WAIT_TIME_MS": 38,
        "DISABLE_ROW_RUNTIME_FILTERING": 39,
        "MAX_NUM_RUNTIME_FILTERS": 40,
        "PARQUET_ANNOTATE_STRINGS_UTF8": 41,
        "PARQUET_FALLBACK_SCHEMA_RESOLUTION": 42,
        "MT_DOP": 43,
        "S3_SKIP_INSERT_STAGING": 44,
        "RUNTIME_FILTER_MAX_SIZE": 45,
        "RUNTIME_FILTER_MIN_SIZE": 46,
        "PREFETCH_MODE": 47,
        "STRICT_MODE": 48,
        "SCRATCH_LIMIT": 49,
        "ENABLE_EXPR_REWRITES": 50,
        "DECIMAL_V2": 51,
        "PARQUET_DICTIONARY_FILTERING": 52,
        "PARQUET_ARRAY_RESOLUTION": 53,
        "PARQUET_READ_STATISTICS": 54,
        "DEFAULT_JOIN_DISTRIBUTION_MODE": 55,
        "DISABLE_CODEGEN_ROWS_THRESHOLD": 56,
        "DEFAULT_SPILLABLE_BUFFER_SIZE": 57,
        "MIN_SPILLABLE_BUFFER_SIZE": 58,
        "MAX_ROW_SIZE": 59,
        "IDLE_SESSION_TIMEOUT": 60,
        "COMPUTE_STATS_MIN_SAMPLE_SIZE": 61,
        "EXEC_TIME_LIMIT_S": 62,
        "SHUFFLE_DISTINCT_EXPRS": 63,
        "MAX_MEM_ESTIMATE_FOR_ADMISSION": 64,
        "THREAD_RESERVATION_LIMIT": 65,
        "THREAD_RESERVATION_AGGREGATE_LIMIT": 66,
        "KUDU_READ_MODE": 67,
        "ALLOW_ERASURE_CODED_FILES": 68,
        "TIMEZONE": 69,
        "SCAN_BYTES_LIMIT": 70,
        "CPU_LIMIT_S": 71,
        "TOPN_BYTES_LIMIT": 72,
        "CLIENT_IDENTIFIER": 73,
        "RESOURCE_TRACE_RATIO": 74,
        "NUM_REMOTE_EXECUTOR_CANDIDATES": 75,
        "NUM_ROWS_PRODUCED_LIMIT": 76,
        "PLANNER_TESTCASE_MODE": 77,
    }


class TInsertResult(object):
    """
    Attributes:
     - rows_modified
     - num_row_errors
    """


    def __init__(self, rows_modified=None, num_row_errors=None,):
        self.rows_modified = rows_modified
        self.num_row_errors = num_row_errors

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.MAP:
                    self.rows_modified = {}
                    (_ktype1, _vtype2, _size0) = iprot.readMapBegin()
                    for _i4 in range(_size0):
                        _key5 = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                        _val6 = iprot.readI64()
                        self.rows_modified[_key5] = _val6
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.num_row_errors = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('TInsertResult')
        if self.rows_modified is not None:
            oprot.writeFieldBegin('rows_modified', TType.MAP, 1)
            oprot.writeMapBegin(TType.STRING, TType.I64, len(self.rows_modified))
            for kiter7, viter8 in self.rows_modified.items():
                oprot.writeString(kiter7.encode('utf-8') if sys.version_info[0] == 2 else kiter7)
                oprot.writeI64(viter8)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.num_row_errors is not None:
            oprot.writeFieldBegin('num_row_errors', TType.I64, 2)
            oprot.writeI64(self.num_row_errors)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.rows_modified is None:
            raise TProtocolException(message='Required field rows_modified is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TPingImpalaServiceResp(object):
    """
    Attributes:
     - version
     - webserver_address
    """


    def __init__(self, version=None, webserver_address=None,):
        self.version = version
        self.webserver_address = webserver_address

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.version = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.webserver_address = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('TPingImpalaServiceResp')
        if self.version is not None:
            oprot.writeFieldBegin('version', TType.STRING, 1)
            oprot.writeString(self.version.encode('utf-8') if sys.version_info[0] == 2 else self.version)
            oprot.writeFieldEnd()
        if self.webserver_address is not None:
            oprot.writeFieldBegin('webserver_address', TType.STRING, 2)
            oprot.writeString(self.webserver_address.encode('utf-8') if sys.version_info[0] == 2 else self.webserver_address)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TResetTableReq(object):
    """
    Attributes:
     - db_name
     - table_name
    """


    def __init__(self, db_name=None, table_name=None,):
        self.db_name = db_name
        self.table_name = table_name

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.db_name = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.table_name = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('TResetTableReq')
        if self.db_name is not None:
            oprot.writeFieldBegin('db_name', TType.STRING, 1)
            oprot.writeString(self.db_name.encode('utf-8') if sys.version_info[0] == 2 else self.db_name)
            oprot.writeFieldEnd()
        if self.table_name is not None:
            oprot.writeFieldBegin('table_name', TType.STRING, 2)
            oprot.writeString(self.table_name.encode('utf-8') if sys.version_info[0] == 2 else self.table_name)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.db_name is None:
            raise TProtocolException(message='Required field db_name is unset!')
        if self.table_name is None:
            raise TProtocolException(message='Required field table_name is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TGetExecSummaryReq(object):
    """
    Attributes:
     - operationHandle
     - sessionHandle
    """


    def __init__(self, operationHandle=None, sessionHandle=None,):
        self.operationHandle = operationHandle
        self.sessionHandle = sessionHandle

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.operationHandle = impala._thrift_gen.TCLIService.ttypes.TOperationHandle()
                    self.operationHandle.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.sessionHandle = impala._thrift_gen.TCLIService.ttypes.TSessionHandle()
                    self.sessionHandle.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('TGetExecSummaryReq')
        if self.operationHandle is not None:
            oprot.writeFieldBegin('operationHandle', TType.STRUCT, 1)
            self.operationHandle.write(oprot)
            oprot.writeFieldEnd()
        if self.sessionHandle is not None:
            oprot.writeFieldBegin('sessionHandle', TType.STRUCT, 2)
            self.sessionHandle.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TGetExecSummaryResp(object):
    """
    Attributes:
     - status
     - summary
    """


    def __init__(self, status=None, summary=None,):
        self.status = status
        self.summary = summary

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.status = impala._thrift_gen.TCLIService.ttypes.TStatus()
                    self.status.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.summary = impala._thrift_gen.ExecStats.ttypes.TExecSummary()
                    self.summary.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('TGetExecSummaryResp')
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.STRUCT, 1)
            self.status.write(oprot)
            oprot.writeFieldEnd()
        if self.summary is not None:
            oprot.writeFieldBegin('summary', TType.STRUCT, 2)
            self.summary.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.status is None:
            raise TProtocolException(message='Required field status is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TGetRuntimeProfileReq(object):
    """
    Attributes:
     - operationHandle
     - sessionHandle
     - format
    """


    def __init__(self, operationHandle=None, sessionHandle=None, format=0,):
        self.operationHandle = operationHandle
        self.sessionHandle = sessionHandle
        self.format = format

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.operationHandle = impala._thrift_gen.TCLIService.ttypes.TOperationHandle()
                    self.operationHandle.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.sessionHandle = impala._thrift_gen.TCLIService.ttypes.TSessionHandle()
                    self.sessionHandle.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.format = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('TGetRuntimeProfileReq')
        if self.operationHandle is not None:
            oprot.writeFieldBegin('operationHandle', TType.STRUCT, 1)
            self.operationHandle.write(oprot)
            oprot.writeFieldEnd()
        if self.sessionHandle is not None:
            oprot.writeFieldBegin('sessionHandle', TType.STRUCT, 2)
            self.sessionHandle.write(oprot)
            oprot.writeFieldEnd()
        if self.format is not None:
            oprot.writeFieldBegin('format', TType.I32, 3)
            oprot.writeI32(self.format)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class TGetRuntimeProfileResp(object):
    """
    Attributes:
     - status
     - profile
     - thrift_profile
    """


    def __init__(self, status=None, profile=None, thrift_profile=None,):
        self.status = status
        self.profile = profile
        self.thrift_profile = thrift_profile

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.status = impala._thrift_gen.TCLIService.ttypes.TStatus()
                    self.status.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.profile = iprot.readString().decode('utf-8', errors='replace') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRUCT:
                    self.thrift_profile = impala._thrift_gen.RuntimeProfile.ttypes.TRuntimeProfileTree()
                    self.thrift_profile.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('TGetRuntimeProfileResp')
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.STRUCT, 1)
            self.status.write(oprot)
            oprot.writeFieldEnd()
        if self.profile is not None:
            oprot.writeFieldBegin('profile', TType.STRING, 2)
            oprot.writeString(self.profile.encode('utf-8') if sys.version_info[0] == 2 else self.profile)
            oprot.writeFieldEnd()
        if self.thrift_profile is not None:
            oprot.writeFieldBegin('thrift_profile', TType.STRUCT, 3)
            self.thrift_profile.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.status is None:
            raise TProtocolException(message='Required field status is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(TInsertResult)
TInsertResult.thrift_spec = (
    None,  # 0
    (1, TType.MAP, 'rows_modified', (TType.STRING, 'UTF8', TType.I64, None, False), None, ),  # 1
    (2, TType.I64, 'num_row_errors', None, None, ),  # 2
)
all_structs.append(TPingImpalaServiceResp)
TPingImpalaServiceResp.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'version', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'webserver_address', 'UTF8', None, ),  # 2
)
all_structs.append(TResetTableReq)
TResetTableReq.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'db_name', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'table_name', 'UTF8', None, ),  # 2
)
all_structs.append(TGetExecSummaryReq)
TGetExecSummaryReq.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'operationHandle', [impala._thrift_gen.TCLIService.ttypes.TOperationHandle, None], None, ),  # 1
    (2, TType.STRUCT, 'sessionHandle', [impala._thrift_gen.TCLIService.ttypes.TSessionHandle, None], None, ),  # 2
)
all_structs.append(TGetExecSummaryResp)
TGetExecSummaryResp.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'status', [impala._thrift_gen.TCLIService.ttypes.TStatus, None], None, ),  # 1
    (2, TType.STRUCT, 'summary', [impala._thrift_gen.ExecStats.ttypes.TExecSummary, None], None, ),  # 2
)
all_structs.append(TGetRuntimeProfileReq)
TGetRuntimeProfileReq.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'operationHandle', [impala._thrift_gen.TCLIService.ttypes.TOperationHandle, None], None, ),  # 1
    (2, TType.STRUCT, 'sessionHandle', [impala._thrift_gen.TCLIService.ttypes.TSessionHandle, None], None, ),  # 2
    (3, TType.I32, 'format', None, 0, ),  # 3
)
all_structs.append(TGetRuntimeProfileResp)
TGetRuntimeProfileResp.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'status', [impala._thrift_gen.TCLIService.ttypes.TStatus, None], None, ),  # 1
    (2, TType.STRING, 'profile', 'UTF8', None, ),  # 2
    (3, TType.STRUCT, 'thrift_profile', [impala._thrift_gen.RuntimeProfile.ttypes.TRuntimeProfileTree, None], None, ),  # 3
)
fix_spec(all_structs)
del all_structs
