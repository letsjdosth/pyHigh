# MPI for python
# https://mpi4py.readthedocs.io/en/stable/index.html

# windows version 지원이 잘 안되는것같음
# (openmpi : NO SUPPORT)
# (MPICH : ONLY OLD VERSION AVAILABLE)

# execution(-n using_core_num):
# $ mpiexec -n 4 python distributed_processing/mpi_ex.py


from mpi4py import MPI

comm = MPI.COMM_WORLD #communicator
rank = comm.Get_rank()
print("This is process", rank)

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=11)
elif rank == 1:
    data = comm.recv(source=0, tag=11)
