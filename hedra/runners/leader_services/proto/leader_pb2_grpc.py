# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from .leader_pb2 import (
        WorkerRegisterRequest,
        WorkerRegisterResponse,
        WorkerUpdateRequest,
        WorkerUpdateResponse,
        WorkerDeregisterRequest,
        WorkerDeregisterResponse,
        LeaderRegisterRequest,
        LeaderRegisterResponse,
        PollLeaderRequest,
        PollLeaderResponse,
        PipelineStageRequest,
        PipelineStageResponse,
        PollLeaderJobRequest,
        PollLeaderJobResponse,
        NewJobLeaderRequest,
        NewJobLeaderResponse,
        LeaderHeartbeatRequest,
        LeaderHeartbeatResponse,
        LeaderJobRequest,
        LeaderJobResponse
)



class DistributedServerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddClient = channel.unary_unary(
                '/DistributedServer/AddClient',
                request_serializer=WorkerRegisterRequest.SerializeToString,
                response_deserializer=WorkerRegisterResponse.FromString,
                )
        self.GetUpdate = channel.unary_unary(
                '/DistributedServer/GetUpdate',
                request_serializer=WorkerUpdateRequest.SerializeToString,
                response_deserializer=WorkerUpdateResponse.FromString,
                )
        self.RemoveClient = channel.unary_unary(
                '/DistributedServer/RemoveClient',
                request_serializer=WorkerDeregisterRequest.SerializeToString,
                response_deserializer=WorkerDeregisterResponse.FromString,
                )
        self.RegisterLeader = channel.unary_unary(
                '/DistributedServer/RegisterLeader',
                request_serializer=LeaderRegisterRequest.SerializeToString,
                response_deserializer=LeaderRegisterResponse.FromString,
                )
        self.PollLeader = channel.unary_unary(
                '/DistributedServer/PollLeader',
                request_serializer=PollLeaderRequest.SerializeToString,
                response_deserializer=PollLeaderResponse.FromString,
                )
        self.MarkStageCompleted = channel.unary_unary(
                '/DistributedServer/MarkStageCompleted',
                request_serializer=PipelineStageRequest.SerializeToString,
                response_deserializer=PipelineStageResponse.FromString,
                )
        self.PollLeaderJob = channel.unary_unary(
                '/DistributedServer/PollLeaderJob',
                request_serializer=PollLeaderJobRequest.SerializeToString,
                response_deserializer=PollLeaderJobResponse.FromString,
                )
        self.CreateNewJob = channel.unary_unary(
                '/DistributedServer/CreateNewJob',
                request_serializer=NewJobLeaderRequest.SerializeToString,
                response_deserializer=NewJobLeaderResponse.FromString,
                )
        self.CheckLeaderHeartbeat = channel.unary_unary(
                '/DistributedServer/CheckLeaderHeartbeat',
                request_serializer=LeaderHeartbeatRequest.SerializeToString,
                response_deserializer=LeaderHeartbeatResponse.FromString,
                )
        self.ShareCurrentJob = channel.unary_unary(
                '/DistributedServer/ShareCurrentJob',
                request_serializer=LeaderJobRequest.SerializeToString,
                response_deserializer=LeaderJobResponse.FromString,
                )


class DistributedServerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddClient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveClient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterLeader(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PollLeader(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MarkStageCompleted(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PollLeaderJob(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateNewJob(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckLeaderHeartbeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ShareCurrentJob(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DistributedServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddClient': grpc.unary_unary_rpc_method_handler(
                    servicer.AddClient,
                    request_deserializer=WorkerRegisterRequest.FromString,
                    response_serializer=WorkerRegisterResponse.SerializeToString,
            ),
            'GetUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUpdate,
                    request_deserializer=WorkerUpdateRequest.FromString,
                    response_serializer=WorkerUpdateResponse.SerializeToString,
            ),
            'RemoveClient': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveClient,
                    request_deserializer=WorkerDeregisterRequest.FromString,
                    response_serializer=WorkerDeregisterResponse.SerializeToString,
            ),
            'RegisterLeader': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterLeader,
                    request_deserializer=LeaderRegisterRequest.FromString,
                    response_serializer=LeaderRegisterResponse.SerializeToString,
            ),
            'PollLeader': grpc.unary_unary_rpc_method_handler(
                    servicer.PollLeader,
                    request_deserializer=PollLeaderRequest.FromString,
                    response_serializer=PollLeaderResponse.SerializeToString,
            ),
            'MarkStageCompleted': grpc.unary_unary_rpc_method_handler(
                    servicer.MarkStageCompleted,
                    request_deserializer=PipelineStageRequest.FromString,
                    response_serializer=PipelineStageResponse.SerializeToString,
            ),
            'PollLeaderJob': grpc.unary_unary_rpc_method_handler(
                    servicer.PollLeaderJob,
                    request_deserializer=PollLeaderJobRequest.FromString,
                    response_serializer=PollLeaderJobResponse.SerializeToString,
            ),
            'CreateNewJob': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNewJob,
                    request_deserializer=NewJobLeaderRequest.FromString,
                    response_serializer=NewJobLeaderResponse.SerializeToString,
            ),
            'CheckLeaderHeartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckLeaderHeartbeat,
                    request_deserializer=LeaderHeartbeatRequest.FromString,
                    response_serializer=LeaderHeartbeatResponse.SerializeToString,
            ),
            'ShareCurrentJob': grpc.unary_unary_rpc_method_handler(
                    servicer.ShareCurrentJob,
                    request_deserializer=LeaderJobRequest.FromString,
                    response_serializer=LeaderJobResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DistributedServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DistributedServer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DistributedServer/AddClient',
            WorkerRegisterRequest.SerializeToString,
            WorkerRegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DistributedServer/GetUpdate',
            WorkerUpdateRequest.SerializeToString,
            WorkerUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DistributedServer/RemoveClient',
            WorkerDeregisterRequest.SerializeToString,
            WorkerDeregisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterLeader(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DistributedServer/RegisterLeader',
            LeaderRegisterRequest.SerializeToString,
            LeaderRegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PollLeader(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DistributedServer/PollLeader',
            PollLeaderRequest.SerializeToString,
            PollLeaderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MarkStageCompleted(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DistributedServer/MarkStageCompleted',
            PipelineStageRequest.SerializeToString,
            PipelineStageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PollLeaderJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DistributedServer/PollLeaderJob',
            PollLeaderJobRequest.SerializeToString,
            PollLeaderJobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateNewJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DistributedServer/CreateNewJob',
            NewJobLeaderRequest.SerializeToString,
            NewJobLeaderResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckLeaderHeartbeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DistributedServer/CheckLeaderHeartbeat',
            LeaderHeartbeatRequest.SerializeToString,
            LeaderHeartbeatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ShareCurrentJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DistributedServer/ShareCurrentJob',
            LeaderJobRequest.SerializeToString,
            LeaderJobResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)