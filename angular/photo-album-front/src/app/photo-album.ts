export interface Task {
  id: number;
  name: string;
  description: string;
  create_date: Date;
  members: Date;
}

    // name = models.CharField(max_length=50)
    // description = models.TextField()
    // create_date = models.DateField(default=date.today)
    // members = models.ManyToManyField(User) #to user
