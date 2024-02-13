class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value=value
        self.next=next
        self.prev=prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur_page=Node(homepage)
        

    def visit(self, url: str) -> None:
        new_page=Node(url)
        self.cur_page.next=new_page
        new_page.prev=self.cur_page
        self.cur_page=new_page
        
    def back(self, steps: int) -> str:
        while self.cur_page.prev and steps: 
            self.cur_page = self.cur_page.prev
            steps-=1
        return self.cur_page.value
        

    def forward(self, steps: int) -> str:
        while self.cur_page.next and steps:
            self.cur_page=self.cur_page.next
            steps-=1
        return self.cur_page.value
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)