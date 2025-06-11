import pytest
from normal_vector import NormalVector

def test_normal_vector_initialization():
    # Test valid initializations
    nv_x = NormalVector(x=1)
    assert nv_x.x == 1
    assert nv_x.y == 0

    nv_y = NormalVector(y=-1)
    assert nv_y.x == 0
    assert nv_y.y == -1

    nv_x_large = NormalVector(x=100)
    assert nv_x_large.x == 1
    assert nv_x_large.y == 0

    nv_y_large = NormalVector(y=-100)
    assert nv_y_large.x == 0
    assert nv_y_large.y == -1
    
    # Test invalid initializations
    with pytest.raises(ValueError):
        NormalVector(x=0, y=0)
    
    with pytest.raises(ValueError):
        NormalVector(x=1, y=1)

    with pytest.raises(ValueError):
        NormalVector(x=-1, y=-1)

def test_normal_vector_repr():
    nv = NormalVector(x=1)
    assert repr(nv) == '[1, 0]'

    nv = NormalVector(y=-1)
    assert repr(nv) == '[0, -1]'

def test_normalize():
    assert NormalVector.normalize(0) == 0
    assert NormalVector.normalize(5) == 1
    assert NormalVector.normalize(-5) == -1
    assert NormalVector.normalize(1) == 1
    assert NormalVector.normalize(-1) == -1

def test_rotate_cw():
    # Start with (1, 0)
    nv = NormalVector(x=1)
    nv.rotate_cw()  # (0, -1)
    assert nv.x == 0
    assert nv.y == -1
    nv.rotate_cw()  # (-1, 0)
    assert nv.x == -1
    assert nv.y == 0
    nv.rotate_cw()  # (0, 1)
    assert nv.x == 0
    assert nv.y == 1
    nv.rotate_cw()  # (1, 0)
    assert nv.x == 1
    assert nv.y == 0

    # Start with (0, 1)
    nv = NormalVector(y=1)
    nv.rotate_cw() # (1,0)
    assert nv.x == 1
    assert nv.y == 0
    nv.rotate_cw() # (0,-1)
    assert nv.x == 0
    assert nv.y == -1

def test_rotate_ccw():
    # Start with (1, 0)
    nv = NormalVector(x=1)
    nv.rotate_ccw()  # (0, 1)
    assert nv.x == 0
    assert nv.y == 1
    nv.rotate_ccw()  # (-1, 0)
    assert nv.x == -1
    assert nv.y == 0
    nv.rotate_ccw()  # (0, -1)
    assert nv.x == 0
    assert nv.y == -1
    nv.rotate_ccw()  # (1, 0)
    assert nv.x == 1
    assert nv.y == 0

    # Start with (0, 1)
    nv = NormalVector(y=1)
    nv.rotate_ccw() # (-1,0)
    assert nv.x == -1
    assert nv.y == 0
    nv.rotate_ccw() # (0,-1)
    assert nv.x == 0
    assert nv.y == -1

def test_add_to():
    nv_x = NormalVector(x=1)
    assert nv_x.add_to(5, 5) == (6, 5)

    nv_y = NormalVector(y=-1)
    assert nv_y.add_to(5, 5) == (5, 4)

    nv_neg_x = NormalVector(x=-1)
    assert nv_neg_x.add_to(0,0) == (-1,0)

    nv_neg_y = NormalVector(y=1)
    assert nv_neg_y.add_to(0,0) == (0,1)

def test_subtract_from():
    nv_x = NormalVector(x=1)
    assert nv_x.subtract_from(5, 5) == (4, 5)

    nv_y = NormalVector(y=-1)
    assert nv_y.subtract_from(5, 5) == (5, 6)

    nv_neg_x = NormalVector(x=-1)
    assert nv_neg_x.subtract_from(0,0) == (1,0)

    nv_neg_y = NormalVector(y=1)
    assert nv_neg_y.subtract_from(0,0) == (0,-1)