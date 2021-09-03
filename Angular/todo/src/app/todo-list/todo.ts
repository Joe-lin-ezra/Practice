export class Todo {
  private title: string = ""
  private completed: boolean = false
  private editable: boolean = false

  constructor(str: string) {
    this.title = str || ''
    this.completed = false
    this.editable = false
  }

  get getTitle(): string {
    return this.title
  }
  setTitle(str: string) {
    this.title = str
  }
  
  toggleCompletion() {
    this.completed = !this.completed
  }
  get getStatus(): boolean {
    return this.completed
  }
  
  get getEditable(): boolean {
    return this.editable
  }
  setEditable(boo: boolean) {
    this.editable = boo
  }
  setCompleted(completed: boolean): void {
    this.completed = completed;
  }
}
