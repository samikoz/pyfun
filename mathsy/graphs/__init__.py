import dependency_injector.providers as providers
import dependency_injector.containers as containers

from mathsy.graphs.graph import _UndirectedGraph
from mathsy.graphs.vertex import Vertex


class VertexFactories(containers.DeclarativeContainer):
    regular = providers.DelegatedFactory(Vertex)


Graph = providers.Factory(
    _UndirectedGraph,
    vertex_factory=VertexFactories.regular
)
