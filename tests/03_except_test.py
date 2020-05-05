"""Basic tests to see if the code raises exceptions."""
import pytest
import logging
import common
from pdb2pqr import cli
from pdb2pqr import main
from pathlib import Path


_LOGGER = logging.getLogger(__name__)
PARSER = cli.build_parser()


def run_pdb2pqr(args, input_pdb, output_pqr, tmp_path_):
    """Basic code for invoking PDB2PQR."""
    arg_str = args + " {inp} {out}"
    output_pqr = tmp_path_ / output_pqr
    _LOGGER.debug("Writing output to %s", output_pqr)
    arg_str = arg_str.format(inp=input_pdb, out=output_pqr)
    args = PARSER.parse_args(arg_str.split())
    main(args)


@pytest.mark.parametrize(
    "args, input_pdb, output_pqr",
    [
        pytest.param(
            "--log-level=INFO --ff=AMBER",
            common.DATA_DIR / "1K1I.pdb",
            "output.pqr",
            id="1K1I AMBER"
        )
    ]
)
def test_ligand(args, input_pdb, input_mol2, output_pqr, tmp_path):
    """Test ligand handling."""
    run_pdb2pqr(args, input_pdb, output_pqr, tmp_path)
    _LOGGER.warning("This test needs better checking to avoid silent failure.")


@pytest.mark.parametrize(
    "args, input_pdb, input_mol2, output_pqr",
    [
        pytest.param(
            "--log-level=INFO --ff=AMBER",
            "1HPX",
            common.DATA_DIR / "1HPX-ligand.mol2",
            "output.pqr",
            id="1HPX-ligand AMBER"
        ),
        pytest.param(
            "--log-level=INFO --ff=AMBER",
            common.DATA_DIR / "1QBS.pdb",
            common.DATA_DIR / "1QBS-ligand.mol2",
            "output.pqr",
            id="1QBS-ligand AMBER"
        ),
        pytest.param(
            "--log-level=INFO --ff=AMBER",
            common.DATA_DIR / "1US0.pdb",
            common.DATA_DIR / "1US0-ligand.mol2",
            "output.pqr",
            id="1US0-ligand AMBER"
        ),
    ]
)
def test_ligand(args, input_pdb, input_mol2, output_pqr, tmp_path):
    """Test ligand handling."""
    args_ = "{args} --ligand={ligand}".format(args=args, ligand=input_mol2)
    run_pdb2pqr(args_, input_pdb, output_pqr, tmp_path)
    _LOGGER.warning("This test needs better checking to avoid silent failure.")