from pathlib import Path
import importlib.util, subprocess, tempfile

spec=importlib.util.spec_from_file_location('vh','tools/verify_handoff.py')
vh=importlib.util.module_from_spec(spec); spec.loader.exec_module(vh)

def run(cwd,*args):
    p=subprocess.run(['git',*args],cwd=cwd,text=True,capture_output=True)
    if p.returncode: raise RuntimeError(p.stdout+p.stderr)
    return p.stdout.strip()

def init_repo(path):
    run(path,'init','-q'); run(path,'config','user.email','a@b.c'); run(path,'config','user.name','test')

def commit(path,name,content):
    (Path(path)/name).write_text(content); run(path,'add',name); run(path,'commit','-qm',content); return run(path,'rev-parse','HEAD')

with tempfile.TemporaryDirectory() as td:
    src=Path(td)/'src'; src.mkdir(); init_repo(src)
    base=commit(src,'f','one')
    head=commit(src,'f','two')
    vh.REPO=src
    w=[]; vh.verify_history_commit(base,required=True,label='base',warnings=w)
    assert not w

    run(src,'checkout','--orphan','other','-q'); run(src,'rm','-q','-f','f'); other=commit(src,'g','other')
    run(src,'checkout','-q','master')
    try:
        vh.verify_history_commit(other,required=True,label='unrelated',warnings=[])
    except AssertionError:
        pass
    else:
        raise AssertionError('unrelated commit was accepted')

    shallow=Path(td)/'shallow'
    run(td,'clone','-q','--depth','1',f'file://{src}',str(shallow))
    vh.REPO=shallow
    w=[]; vh.verify_history_commit(base,required=False,label='released',warnings=w)
    assert w and 'shallow history' in w[0]
    try:
        vh.verify_history_commit(base,required=True,label='held',warnings=[])
    except AssertionError:
        pass
    else:
        raise AssertionError('missing HELD base accepted in shallow clone')

    run(shallow,'checkout','--detach','-q','HEAD')
    w=[]; label=vh.verify_branch_context('master',w)
    assert label=='DETACHED@master' and w

print('VERIFY_HANDOFF_GIT_CONTEXT_TESTS: PASS')
