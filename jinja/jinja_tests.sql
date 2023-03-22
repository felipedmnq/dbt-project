{ % for i in range % }
SELECT { { i } } as number { % if not loop.last % }
union all
{ % endif % } { % endfor % }