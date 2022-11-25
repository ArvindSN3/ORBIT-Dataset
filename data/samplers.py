# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

import random
import numpy as np
from torch.utils.data.sampler import Sampler

class TaskSampler(Sampler):
    """
    Sampler class for a fixed number of tasks per user. 
    """
    def __init__(self, tasks_per_user, num_users, shuffle):
        """
        Creates instances of TaskSampler.
        :param tasks_per_user: (int) Number of tasks to sample per user.
        :param num_users: (int) Total number of users.
        :param shuffle: (bool) If True, shuffle tasks, otherwise do not shuffle.
        :return: Nothing.
        """
        self.tasks_per_user = tasks_per_user
        self.num_users = num_users
        self.shuffle = shuffle

    def __iter__(self):
        task_ids = []
        for user in range(self.num_users):
            task_ids.extend([user]*self.tasks_per_user)
        if self.shuffle:
            random.shuffle(task_ids)
        return iter(task_ids)

    def __len__(self):
        return self.num_users*self.tasks_per_user
