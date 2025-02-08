#Importing pytest
import pytest
from water_flow import pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction, pressure_loss_from_pipe

def test_pressure_loss_from_fittings():
    
    assert pytest.approx(pressure_loss_from_fittings(0.00, 3), abs=0.001) == 0.000
    
    assert pytest.approx(pressure_loss_from_fittings(1.65, 0), abs=0.001) == 0.000
    
    assert pytest.approx(pressure_loss_from_fittings(1.65, 2), abs=0.001) == -0.109
    
    assert pytest.approx(pressure_loss_from_fittings(1.75, 2), abs=0.001) == -0.122
    
    assert pytest.approx(pressure_loss_from_fittings(1.75, 5), abs=0.001) == -0.306

def test_reynolds_number():
    
    assert pytest.approx(reynolds_number(0.048692, 0.00), abs=1) == 0
    
    assert pytest.approx(reynolds_number(0.048692, 1.65), abs=1) == 80069
    
    assert pytest.approx(reynolds_number(0.048692, 1.75), abs=1) == 84922
    
    assert pytest.approx(reynolds_number(0.286870, 1.65), abs=1) == 471729
    
    assert pytest.approx(reynolds_number(0.286870, 1.75), abs=1) == 500318

def test_pressure_loss_from_pipe_reduction():
    assert pytest.approx(pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692), abs=0.001) == 0.000

    loss1 = pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692)
    assert pytest.approx(loss1, abs=0.001) == loss1

    loss2 = pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692)
    assert pytest.approx(loss2, abs=0.001) == loss2

def test_pressure_loss_from_pipe():
    loss1 = pressure_loss_from_pipe(0.28687, 10, 0.013, 1.65)
    assert pytest.approx(loss1, abs=0.01) == loss1

    loss2 = pressure_loss_from_pipe(0.048692, 5, 0.018, 1.75)
    assert pytest.approx(loss2, abs=0.01) == loss2

    
if __name__ == "__main__":
    pytest.main()