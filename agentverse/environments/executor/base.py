from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, List, Tuple, Any

from pydantic import BaseModel

from agentverse.agents import ExecutorAgent

from . import executor_registry


class BaseExecutor(BaseModel):
    """
    The base class of execution.
    """

    def step(
        self,
        agent: ExecutorAgent,
        task_description: str,
        solution: List[str],
        *args,
        **kwargs,
    ) -> Any:
        pass

    async def astep(
        self,
        agent: ExecutorAgent,
        task_description: str,
        solution: List[str],
        *args,
        **kwargs,
    ) -> Any:
        pass

    def reset(self):
        pass


@executor_registry.register("none")
class NoneExecutor(BaseExecutor):
    """
    The base class of execution.
    """

    def step(
        self,
        agent: ExecutorAgent,
        task_description: str,
        solution: List[str],
        *args,
        **kwargs,
    ) -> Any:
        return "None"

    def reset(self):
        pass
