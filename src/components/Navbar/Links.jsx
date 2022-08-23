export const Links = ({ linkName = "Error" }) => {
  return (
    <div className="py-2">
      <a className="hover:text-pink-500  md:visible lg:visible" href="">
        {linkName}
      </a>
    </div>
  );
};
