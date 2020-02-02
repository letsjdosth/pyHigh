# for test using pytest of 'simul.py'

from simul import Particle, ParticleSimulator

def test_evolve(benchmark):
    particles = [Particle(0.3, 0.5, +1), Particle(0.0, -0.5, -1), Particle(-0.1, -0.4, +3)]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)

    p0, p1, p2 = particles

    def fequal(a,b, eps=1e-5):
        return abs(a-b) < eps

    assert fequal(p0.x, 0.210269)
    assert fequal(p0.y, 0.543863)

    assert fequal(p1.x, -0.099334)
    assert fequal(p1.y, -0.490034)

    assert fequal(p2.x, 0.191372) #책과 다름
    assert fequal(p2.y, -0.365330) #책과 다름

    benchmark(simulator.evolve, 0.1)

# 1. 벤치마크 픽스쳐 없을 시(test_evolve의 benchmark 인자 및 24번째줄 제거시)
# $ pytest benchmarking_profiling/simul_bench_pytest.py::test_evolve
# ====== test session starts =========================================================================================
# platform win32 -- Python 3.7.5, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
# rootdir: C:\gitProject\pyHigh
# collected 1 item                                                                                                                                                                                      

# benchmarking_profiling\simul_bench_pytest.py .                                                                                                                                                  [100%]

# ====== 1 passed in 0.30s ==========================================================================================


# 2. 벤치마크 픽스쳐 사용시(pytest-benchmark 플러그인 사용)
# $ pytest benchmarking_profiling/simul_bench_pytest.py::test_evolve
# ====== test session starts =========================================================================================
# platform win32 -- Python 3.7.5, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
# benchmark: 3.2.3 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
# rootdir: C:\gitProject\pyHigh
# plugins: benchmark-3.2.3
# collected 1 item                                                                                                                                                                                      

# benchmarking_profiling\simul_bench_pytest.py .                                                                                                                                                  [100%]


# -------------------------------------------- benchmark: 1 tests --------------------------------------------
# Name (time in ms)        Min     Max    Mean  StdDev  Median     IQR  Outliers       OPS  Rounds  Iterations
# ------------------------------------------------------------------------------------------------------------
# test_evolve           2.1215  3.0451  2.2078  0.0919  2.1736  0.0578     34;34  452.9319     414           1
# ------------------------------------------------------------------------------------------------------------

# Legend:
#   Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
# ====== 1 passed in 2.23s ==========================================================================================

# Round횟수만큼 실행하여 그 통계값을 제공