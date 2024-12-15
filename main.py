import threading
import time
from queue import Queue


class Task:
    def __init__(self, id, duration):
        self.id = id
        self.duration = duration


class Worker(threading.Thread):
    def __init__(self, identificator, performance):
        super().__init__()
        self.id = identificator
        self.performance = performance  # Производительность процесса
        self.task_queue = Queue()
        self.remaining_time = 0  # Общее время выполнения задач

    def run(self):
        while True:
            task = self.task_queue.get()
            if task is None:  # Проверка на завершение работы
                break

            time_to_complete = round(task.duration / self.performance)
            print(
                f"\nWorker {self.id} started task {task.id} (duration: {task.duration}, performance: {self.performance})")
            while time_to_complete:
                time.sleep(1)
                time_to_complete = time_to_complete - 1
                self.remaining_time = self.remaining_time - 1
            # time.sleep(time_to_complete)  # Симуляция выполнения задачи
            print(f"\nWorker {self.id} finished task {task.id}")
            self.task_queue.task_done()

    def add_task(self, task):
        self.task_queue.put(task)
        if task is not None:
            self.remaining_time += round(task.duration / self.performance)


    def get_remaining_time(self):
        return self.remaining_time

    def get_queue_length(self):
        return self.task_queue.qsize()


def main():
    num_workers = int(input("Enter the number of workers: "))  # Количество рабочих процессов
    workers = []

    for i in range(num_workers):  # Задание производительности рабочих процессов
        performance = float(input(f"Enter performance for Process {i + 1}: "))
        workers.append(Worker(i, performance))

    for worker in workers:
        worker.start()

    task_number = 0
    while True:  # Генерация задач пользователем
        command = input("Enter a command (add_task/check_status/exit): ").strip().lower()

        if command == "add_task":
            complexity = float(input("Enter task complexity: "))
            task = Task(task_number, complexity)
            task_number += 1
            min_worker = min(workers, key=lambda w: w.get_remaining_time())
            min_worker.add_task(task)

        elif command == "check_status":
            for worker in workers:
                print(
                    f"Process {worker.id}: Remaining Time: {worker.get_remaining_time()}, Queue Length: {worker.get_queue_length()}")

        elif command == "exit":
            print("Exiting the simulation.")
            # Завершение работы рабочих процессов
            for worker in workers:
                worker.add_task(None)  # Отправляем сигнал о завершении работы после выполнения всех задач
            for worker in workers:
                worker.join()  # Ждем завершения потоков
            break

        else:
            print("Unknown command. Please enter 'add_task', 'check_status', or 'exit'.")


if __name__ == "__main__":
    main()
