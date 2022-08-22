from toysql.page import Page, PageType, LeafPageCell
from toysql.exceptions import PageFullException, PageNotFoundException, NotFoundException

class BPlusTree:
    """
    All leaves are at the same level.

    The root has at least two children.

    Each node except root can have a maximum of m children and at least m/2 children.

    Each node can contain a maximum of m - 1 keys and a minimum of ⌈m/2⌉ - 1 keys.

    btree degree: represents the lower bound on the number of children a node in the B Tree can have (except for the root). i.e the minimum number of children possible.

    btree order: represents the upper bound on the number of children. ie. the maximum number possible.
    """
    def __init__(self, page_number, pager, order=4) -> None:
        self.pager = pager 
        self.root = pager.read_page(page_number)
        self.order = order 

    def add(self, values) -> None:
        """
        This adds a tuple value to the tree. 
        """
        cell = LeafPageCell(values)
        page = self._search(cell.row_id, self.root)
        assert page is not None

        if self.pager.page_size - len(page) < len(cell):
            # Page is full.
           [left, right] = self._split(page)

        self.root.add_cell(cell)

    def search(self, key):
        page = self._search(key, self.root)
        if page:
            cell = page.find_cell(key)
            if not cell:
                raise NotFoundException
            return cell
        else:
            raise NotFoundException

    def _split(self, page):

        #[left_cells, right_cells] =   
        return []

    def _search(self, key, page: Page):
        if page.page_type == PageType.leaf:
            return page

        for i, cell in enumerate(page.cells):
            if cell[] > cell.row_id:
                return self._search(self.pager.read_page(cell.left_child_page_number), cell.row_id)
