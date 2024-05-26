from wolfram_sigma_backend.app.domain.matrix import MatrixSchema
from wolfram_sigma_backend.app.infrastructure.math.matrix_processor import (
    MatrixProcessorFromCLib,
)
from wolfram_sigma_backend.app.web_api.equations.router import equations_router


@equations_router.post("definite_integral")
def definite_integral():
    ...
