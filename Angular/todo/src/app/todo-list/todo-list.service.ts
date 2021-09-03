import { Injectable } from '@angular/core';
import { Todo } from './todo';
import { TodoStatus } from './todo-status';

@Injectable({
  providedIn: 'root'
})
export class TodoListService {

  private list: Todo[] = []

  constructor() { }

  add(str: string): void {
    this.list.push(new Todo(str))
  }

  getList(): Todo[] {
    return this.list
  }
  getActiveList(): Todo[] {
    return this.list.filter(todo => todo.getStatus === false)
  }
  getDoneList(): Todo[] {
    return this.list.filter(todo => todo.getStatus === true)
  }

  remove(index: number): void {
    this.list.splice(index, 1);
  }
  removeCompletedList() {
    this.list = this.list.filter(todo => todo.getStatus == false)
  }
}