from random import uniform

from matplotlib import pyplot as plt
from matplotlib import animation

class Particle:
    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel

class ParticleSimulator:
    def __init__(self, particles):
        self.particles = particles

    def evolve(self, dt):
        timestep = 0.0001
        nsteps = int(dt / timestep)

        for i in range(nsteps):
            for p in self.particles:
                # 방향
                norm = (p.x**2 + p.y**2)**0.5
                v_x = -p.y / norm
                v_y = p.x / norm

                #변위
                d_x = timestep * p.ang_vel * v_x
                d_y = timestep * p.ang_vel * v_y

                p.x += d_x
                p.y += d_y
    
    def evolve_fast(self, dt):
        timestep = 0.0001
        nsteps = int(dt / timestep)

        for p in self.particles:
            t_x_ang = timestep * p.ang_vel
            for i in range(nsteps):
                norm = (p.x**2 + p.y**2)**0.5

                p.x = p.x - t_x_ang * p.y / norm
                p.y = p.y + t_x_ang * p.x / norm

def visualize(simulator):
    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    line, = ax.plot(X, Y, 'ro')

    plt.xlim(-1,1)
    plt.ylim(-1,1)

    def init():
        line.set_data([],[])
        return line,
    
    def animate(i):
        simulator.evolve(0.01)
        X = [p.x for p in simulator.particles]
        Y = [p.y for p in simulator.particles]

        line.set_data(X,Y)
        return line,
    
    anim = animation.FuncAnimation(fig=fig, func=animate, init_func = init, blit=True, interval=10)
    plt.show()

# for main execution
def test_visualize():
    particles = [Particle(0.3, 0.5, 1), Particle(0.0, -0.5, -1), Particle(-0.1, -0.4, 3)]
    simulator = ParticleSimulator(particles)
    visualize(simulator)


# test suit
def test_evolve():
    particles = [Particle(0.3, 0.5, 1), Particle(0.0, -0.5, -1), Particle(-0.1, -0.4, 3)]
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

# benchmark
def benchmark():
    particles = [Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), uniform(-1.0, 1.0)) for i in range(1000)]
    simulator = ParticleSimulator(particles)
    simulator.evolve(0.1)

# if __name__ == '__main__':
    # test_visualize()
    # test_evolve()
    # benchmark()
    
    # unix의 time 이용:  윈도우에서는 잘 동작하지 않을 수 있음(unix 명령. bash가 제대로 구현했는지 모르겠음)
    # $ time python benchmarking_profiling/simul.py 
    # real    0m1.103s //<-프로세스 실행 시작~끝
    # user    0m0.000s //<-계산 cpu time (흠 왜 0일까?)
    # sys     0m0.016s //<-메모리 할당 등 시스템 연관작업에의 cpu time

    # timeit 모듈 이용
    # import timeit
    # bench_result = timeit.timeit('benchmark()', setup='from __main__ import benchmark', number=10)
