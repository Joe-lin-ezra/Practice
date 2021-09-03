import { Component, OnInit } from '@angular/core';
import { TodoListService } from './todo-list.service';
import { Todo } from './todo'
import { TodoStatus } from './todo-status';

@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.css']
})
export class TodoListComponent implements OnInit {

  public todoStatus = TodoStatus
  private status: TodoStatus = TodoStatus.all

  constructor(private todoListService: TodoListService) { }

  ngOnInit(): void {
  }

  setStatus(s: TodoStatus) {
    this.status = s
  }

  checkStatus(s: TodoStatus): boolean {
    return this.status === s
  }

  /**
   * new to do event
   * @param input: the string inputted by user 
   */
  addTodo(input: HTMLInputElement): void {
    if (!input) {
      return 
    }
    const todo = input.value.trim()
    if (todo) {
      this.todoListService.add(todo)
    }
    input.value = ""
  }
  getList(): Todo[] {
    let l: Todo[] = []
    switch (this.status) {
      case this.todoStatus.all:
        l = this.todoListService.getList()
        break
      case this.todoStatus.active:
        l = this.todoListService.getActiveList()
        break
      case this.todoStatus.done:
        l = this.todoListService.getDoneList()
        break
    }
    return l
  }
  getRemainingList(): Todo[] {
    return this.todoListService.getActiveList()
  }
  getDoneList(): Todo[] {
    return this.todoListService.getDoneList()
  }

  remove(index: number): void {
    console.log("remove", index)
    this.todoListService.remove(index)
  }
  removeCompletedList(): void {
    this.todoListService.removeCompletedList()
  }

  edit(todo: Todo) {
    todo.setEditable(true)
  }
  cancelEdit(todo: Todo) {
    todo.setEditable(false)
  }

  update(todo: Todo, newTitle: string): void {
    console.log("console: ", todo.getTitle, newTitle)
    if (!newTitle.trim() || !todo.getEditable) {
      todo.setEditable(false)
      return ;
    }
    else {
      todo.setTitle(newTitle)
      todo.setEditable(false)
    }
  }

  isAllCompleted(): boolean {
    return this.todoListService.getDoneList().length ==
     this.todoListService.getList().length
  }

  setAllTo(boo: boolean): void {
    this.todoListService.getList().forEach(i => i.setCompleted(boo))
  }
}
