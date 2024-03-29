# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import pokemonou_pb2 as pokemonou__pb2


class PokemonOUGameStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Board = channel.unary_unary(
                '/ou_pokemon.PokemonOUGame/Board',
                request_serializer=pokemonou__pb2.Player.SerializeToString,
                response_deserializer=pokemonou__pb2.InitialMoves.FromString,
                )
        self.Checkboard = channel.unary_unary(
                '/ou_pokemon.PokemonOUGame/Checkboard',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=pokemonou__pb2.MoveDecision.FromString,
                )
        self.TrainerMove = channel.unary_unary(
                '/ou_pokemon.PokemonOUGame/TrainerMove',
                request_serializer=pokemonou__pb2.TrainMove.SerializeToString,
                response_deserializer=pokemonou__pb2.Message.FromString,
                )
        self.Trainer = channel.unary_unary(
                '/ou_pokemon.PokemonOUGame/Trainer',
                request_serializer=pokemonou__pb2.TrainerName.SerializeToString,
                response_deserializer=pokemonou__pb2.TrainerInfo.FromString,
                )
        self.TrainerPath = channel.unary_unary(
                '/ou_pokemon.PokemonOUGame/TrainerPath',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=pokemonou__pb2.MoveList.FromString,
                )
        self.Captured = channel.unary_unary(
                '/ou_pokemon.PokemonOUGame/Captured',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=pokemonou__pb2.Message.FromString,
                )
        self.PokemonMove = channel.unary_unary(
                '/ou_pokemon.PokemonOUGame/PokemonMove',
                request_serializer=pokemonou__pb2.PokMove.SerializeToString,
                response_deserializer=pokemonou__pb2.Message.FromString,
                )
        self.Pokedex = channel.unary_unary(
                '/ou_pokemon.PokemonOUGame/Pokedex',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=pokemonou__pb2.PokemonList.FromString,
                )
        self.PokemonPath = channel.unary_unary(
                '/ou_pokemon.PokemonOUGame/PokemonPath',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=pokemonou__pb2.MoveList.FromString,
                )


class PokemonOUGameServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Board(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Checkboard(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TrainerMove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Trainer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TrainerPath(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Captured(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PokemonMove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Pokedex(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PokemonPath(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PokemonOUGameServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Board': grpc.unary_unary_rpc_method_handler(
                    servicer.Board,
                    request_deserializer=pokemonou__pb2.Player.FromString,
                    response_serializer=pokemonou__pb2.InitialMoves.SerializeToString,
            ),
            'Checkboard': grpc.unary_unary_rpc_method_handler(
                    servicer.Checkboard,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=pokemonou__pb2.MoveDecision.SerializeToString,
            ),
            'TrainerMove': grpc.unary_unary_rpc_method_handler(
                    servicer.TrainerMove,
                    request_deserializer=pokemonou__pb2.TrainMove.FromString,
                    response_serializer=pokemonou__pb2.Message.SerializeToString,
            ),
            'Trainer': grpc.unary_unary_rpc_method_handler(
                    servicer.Trainer,
                    request_deserializer=pokemonou__pb2.TrainerName.FromString,
                    response_serializer=pokemonou__pb2.TrainerInfo.SerializeToString,
            ),
            'TrainerPath': grpc.unary_unary_rpc_method_handler(
                    servicer.TrainerPath,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=pokemonou__pb2.MoveList.SerializeToString,
            ),
            'Captured': grpc.unary_unary_rpc_method_handler(
                    servicer.Captured,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=pokemonou__pb2.Message.SerializeToString,
            ),
            'PokemonMove': grpc.unary_unary_rpc_method_handler(
                    servicer.PokemonMove,
                    request_deserializer=pokemonou__pb2.PokMove.FromString,
                    response_serializer=pokemonou__pb2.Message.SerializeToString,
            ),
            'Pokedex': grpc.unary_unary_rpc_method_handler(
                    servicer.Pokedex,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=pokemonou__pb2.PokemonList.SerializeToString,
            ),
            'PokemonPath': grpc.unary_unary_rpc_method_handler(
                    servicer.PokemonPath,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=pokemonou__pb2.MoveList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ou_pokemon.PokemonOUGame', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PokemonOUGame(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Board(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ou_pokemon.PokemonOUGame/Board',
            pokemonou__pb2.Player.SerializeToString,
            pokemonou__pb2.InitialMoves.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Checkboard(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ou_pokemon.PokemonOUGame/Checkboard',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            pokemonou__pb2.MoveDecision.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TrainerMove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ou_pokemon.PokemonOUGame/TrainerMove',
            pokemonou__pb2.TrainMove.SerializeToString,
            pokemonou__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Trainer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ou_pokemon.PokemonOUGame/Trainer',
            pokemonou__pb2.TrainerName.SerializeToString,
            pokemonou__pb2.TrainerInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TrainerPath(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ou_pokemon.PokemonOUGame/TrainerPath',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            pokemonou__pb2.MoveList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Captured(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ou_pokemon.PokemonOUGame/Captured',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            pokemonou__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PokemonMove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ou_pokemon.PokemonOUGame/PokemonMove',
            pokemonou__pb2.PokMove.SerializeToString,
            pokemonou__pb2.Message.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Pokedex(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ou_pokemon.PokemonOUGame/Pokedex',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            pokemonou__pb2.PokemonList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PokemonPath(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ou_pokemon.PokemonOUGame/PokemonPath',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            pokemonou__pb2.MoveList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
